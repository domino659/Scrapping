from time import sleep
from sys import exit
from pandas import isna
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from utils.json_loader import get_web_data
from utils.xlsx_manager import open_xlsx, modify_xlsx
from utils.captcha.captcha_text import detect_capcha
from utils.log import *
from utils.scrapping.bs4 import table_scrap
from variable import PATH_CHROMEDRIVER

file_name = "data_hp.xlsx"


def scrapping_hp():
    number_index = 0
    # Extract data from json
    data = open_xlsx(file_name)

    # Create lists with serial numbers and product numbers
    serial_numbers = list(data["serial_number"].values())
    if isna(serial_numbers).any():
        logging.info("Can't take empty serial number.")
        exit("Can't take empty serial number.")

    product_numbers = list(data["product_number"].values())
    if isna(product_numbers).any():
        logging.info("Can't take empty product number.")
        exit("Can't take empty product number.")

    # Create Selenium Driver
    driver = webdriver.Chrome(PATH_CHROMEDRIVER)
    wait = WebDriverWait(driver, 20)

    # Splice lists 20 by 20 as hp site can't get more than 20 input at a time
    while number_index < (len(serial_numbers)-1):
        logging.info("Scrapping Started.")
        serial_numbers_batch = serial_numbers[number_index:number_index+20]
        product_numbers_batch = product_numbers[number_index:number_index+20]

        # Load Page
        driver.get(get_web_data()["hp"]["website"]["warrenty_check"])

        # In case their is more than 10 product
        if len(serial_numbers_batch) > 10:
            wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[@id='wcFormDataItem']/span/a")))
            add_more_serial_number = driver.find_element_by_xpath(
                "//*[@id='wcFormDataItem']/span/a")
            add_more_serial_number.click()

        # Enter serial number for all product
        for i in range(len(serial_numbers_batch)):
            wait.until(EC.element_to_be_clickable((
                By.ID, f"serialNumber{i}")))
            serial_number_search_bar = driver.find_element_by_id(
                f"serialNumber{i}")
            serial_number_search_bar.send_keys(serial_numbers_batch[i])
            i += 1
        serial_number_search_bar.send_keys(Keys.ENTER)

        detect_capcha(driver)

        # Enter product number for all product if needed
        try:
            for i in range(len(product_numbers_batch)):
                try:
                    product_number_search_bar = driver.find_element_by_id(
                        f"productNumber{i}")
                    product_number_search_bar.send_keys(
                        product_numbers_batch[i])
                except NoSuchElementException:
                    pass
                i += 1
            try:
                product_number_search_bar.send_keys(Keys.ENTER)
            except StaleElementReferenceException:
                pass
        except UnboundLocalError:
            pass

        detect_capcha(driver)

        # Iterate througt each detailed list to scrap infomation
        for i in range(len(serial_numbers_batch)):
            wait.until(EC.element_to_be_clickable((
                By.XPATH, f"//*[@id='details_link_{serial_numbers_batch[i]}']/a")))
            product_detail = driver.find_element_by_xpath(
                f"//*[@id='details_link_{serial_numbers_batch[i]}']/a")
            product_detail.click()

            # Scrap contract information
            wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[@id='introBlock']/table[1]")))
            contrat_assistance = driver.find_element_by_xpath(
                "//*[@id='introBlock']/table[1]").get_attribute('innerHTML')
            data_contrat_assistance = table_scrap(contrat_assistance)

            # Scrap garantie information
            wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[@id='introBlock']/table[2]")))
            garantie = driver.find_element_by_xpath(
                "//*[@id='introBlock']/table[2]").get_attribute('innerHTML')
            data_garantie = table_scrap(garantie)

            # Transform scraped data into a dict that will be converted into a
            # dataframe and then entered in the xlsx document
            modify_xlsx(data_contrat_assistance,
                        data_garantie, number_index, file_name)

            # Log for each product scrapped
            logging.info(f"Index {number_index} is being processed.")

            # DEBUG
            print(f"Current batch: {i}")
            print(f"Index: {number_index}")

            # Go back to precedent menu
            wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[@id='body']/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div[2]/input")))
            back_to_menu = driver.find_element_by_xpath(
                "//*[@id='body']/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div[2]/input")
            back_to_menu.click()
            i += 1
            number_index += 1
    driver.quit()
