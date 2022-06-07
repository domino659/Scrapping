from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from utils.json_loader import get_web_data
from utils.captcha.captcha_text import detect_capcha

DRIVER_PATH = "C:/ChromeDriver/chromedriver.exe"

def hp_warrenty_check():
    number_index = 0
    # Extract data from json
    data = get_web_data()["hp"]["data"]
    serial_numbers = []
    product_numbers = []
    for i in data:
        serial_numbers.append(data[i]["serial_number"])
        product_numbers.append(data[i]["product_number"])
        i=+1

    driver = webdriver.Chrome(DRIVER_PATH)
    
    # Splice them 20 by 20 as hp site can't get more than 20 input
    while number_index < len(serial_numbers):
        serial_numbers_batch = serial_numbers[number_index:number_index+20]
        product_numbers_batch = product_numbers[number_index:number_index+20]
        # Load Page
        sleep(randint(2,3))
        driver.get(get_web_data()["hp"]["website"]["warrenty_check"])

        # In case their is more than 10 product
        if len(serial_numbers_batch) > 10:
            add_more_serial_number = driver.find_element_by_link_text("Ajouter d'autres garanties")
            add_more_serial_number.click()

        # Enter serial number for all product
        for i in range(len(serial_numbers_batch)):
            serial_number_search_bar = driver.find_element_by_id(f"serialNumber{i}")
            serial_number_search_bar.send_keys(serial_numbers_batch[i])
            i+=1
        serial_number_search_bar.send_keys(Keys.ENTER)

        sleep(randint(2,3))

        detect_capcha(driver)
        
        # Enter product number for all product
        try:
            for i in range(len(product_numbers_batch)):
                try:
                    product_number_search_bar = driver.find_element_by_id(f"productNumber{i}")
                    product_number_search_bar.send_keys(product_numbers_batch[i])
                except NoSuchElementException:
                    pass
                i+=1
            try:
                product_number_search_bar.send_keys(Keys.ENTER)
            except StaleElementReferenceException:
                pass
        except UnboundLocalError:
            pass


        sleep(randint(2,3))

        detect_capcha(driver)

        # Iterate througt each detail list to scrap infomation
        for i in range(len(serial_numbers_batch)):
            product_detail = driver.find_element_by_id(f"details_link_{serial_numbers_batch[i]}")
            product_detail_link = product_detail.find_element_by_link_text("Afficher les détails")
            product_detail_link.click()

            # Log into file each product scrapped
            # DEBUG
            print(i)
            print(f"number index {number_index}")
            
            sleep(2)
            back_to_menu = driver.find_element_by_xpath("//*[@id='body']/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div[2]/input")
            back_to_menu.click()
            i+= 1
            number_index += 1

hp_warrenty_check()







# def hp_part_surfer():
#     driver.get(get_web_data()["hp"]["website"]["part_surfer"])

#     sleep(randint(3,4))
    
#     country_drop_down = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")
#     selected_country_drop_down = Select(country_drop_down)
#     selected_country_drop_down.select_by_visible_text("France")
#     serial_number_search_bar = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_SearchText_TextBox1")
#     serial_number_search_bar.send_keys(get_web_data()["hp"]["data"]["0"]["serial_number"])
#     serial_number_search_bar.send_keys(Keys.ENTER)