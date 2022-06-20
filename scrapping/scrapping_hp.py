from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from utils.json_loader import get_web_data
from utils.xlsx_manager import open_xlsx
from utils.captcha.captcha_text import detect_capcha
from utils.log import *
from utils.text_modifier import simplify
from utils.scrapping.bs4 import table_scrap

DRIVER_PATH = "C:/ChromeDriver/chromedriver.exe"


def hp_warrenty_check():
    number_index = 0
    # Extract data from json
    data = open_xlsx()
    serial_numbers = list(data["serial_number"].values())
    print(serial_numbers)
    product_numbers = list(data["product_number"].values())

    driver = webdriver.Chrome(DRIVER_PATH)
    # Splice them 20 by 20 as hp site can't get more than 20 input
    while number_index < (len(serial_numbers)-1):
        logging.info("Scrapping Started.")
        serial_numbers_batch = serial_numbers[number_index:number_index+20]
        product_numbers_batch = product_numbers[number_index:number_index+20]
        # Load Page
        sleep(2)
        driver.get(get_web_data()["hp"]["website"]["warrenty_check"])

        # In case their is more than 10 product
        if len(serial_numbers_batch) > 10:
            add_more_serial_number = driver.find_element_by_link_text(
                "Ajouter d'autres garanties")
            add_more_serial_number.click()

        # Enter serial number for all product
        for i in range(len(serial_numbers_batch)):
            serial_number_search_bar = driver.find_element_by_id(
                f"serialNumber{i}")
            serial_number_search_bar.send_keys(serial_numbers_batch[i])
            i += 1
        serial_number_search_bar.send_keys(Keys.ENTER)

        sleep(2)

        detect_capcha(driver)

        # Enter product number for all product
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

        sleep(2)

        detect_capcha(driver)

        # Iterate througt each detail list to scrap infomation
        for i in range(len(serial_numbers_batch)):
            sleep(3)
            product_detail = driver.find_element_by_id(
                f"details_link_{serial_numbers_batch[i]}")
            product_detail_link = product_detail.find_element_by_link_text(
                "Afficher les détails")
            product_detail_link.click()

            sleep(2)

            contrat_assistance = driver.find_element_by_xpath(
                "//*[@id='introBlock']/table[1]").get_attribute('innerHTML').encode('utf-8')
            print("UNTOUCHED DATA")
            print(type(contrat_assistance))
            print(contrat_assistance)
            data_contrat_assistance = table_scrap(contrat_assistance)
            print("DATA")
            print(data_contrat_assistance)

            garantie = driver.find_element_by_xpath(
                "//*[@id='introBlock']/table[2]").get_attribute('innerHTML').encode('utf-8')

            # data_garantie = table_scrap(garantie)
            # print(data_garantie)

            # Log into file each product scrapped
            # DEBUG
            logging.info(f"Index number {number_index} is being processed.")

            print(i)
            print(f"number index {number_index}")

            sleep(2)
            back_to_menu = driver.find_element_by_xpath(
                "//*[@id='body']/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div[2]/input")
            back_to_menu.click()
            i += 1
            number_index += 1


# def hp_part_surfer():
#     driver.get(get_web_data()["hp"]["website"]["part_surfer"])

#     sleep(randint(3,4))

#     country_drop_down = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")
#     selected_country_drop_down = Select(country_drop_down)
#     selected_country_drop_down.select_by_visible_text("France")
#     serial_number_search_bar = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_SearchText_TextBox1")
#     serial_number_search_bar.send_keys(get_web_data()["hp"]["data"]["0"]["serial_number"])
#     serial_number_search_bar.send_keys(Keys.ENTER)
