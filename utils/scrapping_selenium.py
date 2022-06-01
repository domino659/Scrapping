from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from utils.json_loader import get_web_data

# Or https://partsurfer.hpe.com/Search.aspx?SearchText=CZJ029073S
DRIVER_PATH = "C:/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)

def detect_capcha():
    try:
        captcha = driver.find_element_by_id("captchaForm")
        if captcha: {
            capcha()
        }
    except NoSuchElementException:
        pass

def capcha():

    sleep(2)

    driver.find_element_by_id("captchaImg").screenshot('img/captcha_screenshot.png')
    
    captcha_text = resolve()

    captcha = driver.find_element_by_id("captchaChars")
    captcha.send_keys(captcha_text)

def resolve():
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string('img/captcha_screenshot.png')
    
    # DEBUG
    # print(result)
    
    return result

def hp_warrenty_check():
    driver.get(get_web_data()["hp"]["website"]["warrenty_check"])
    
    sleep(randint(2,3))

    data = get_web_data()["hp"]["data"]
    serial_numbers = []
    product_numbers = []
    for i in data:
        serial_numbers.append(data[i]["serial_number"])
        product_numbers.append(data[i]["product_number"])
        i=+1

    # serial_number_index = 0
    # while serial_number_index < len(serial_numbers):
    #     serial_numbers_batch = serial_numbers[serial_number_index:serial_number_index+20]
    #     serial_number_index += 20



    # In case their is more than 10 product
    if len(serial_numbers) > 10:
        add_more_serial_number = driver.find_element_by_link_text("Ajouter d'autres garanties")
        add_more_serial_number.click()

    for i in range(len(serial_numbers)):
        serial_number_search_bar = driver.find_element_by_id(f"serialNumber{i}")
        serial_number_search_bar.send_keys(serial_numbers[i])
        i+=1
    serial_number_search_bar.send_keys(Keys.ENTER)

    sleep(randint(2,3))

    detect_capcha()
    
    for i in range(len(product_numbers)):
        try:
            product_number_search_bar = driver.find_element_by_id(f"productNumber{i}")
            product_number_search_bar.send_keys(product_numbers[i])
        except NoSuchElementException:
            pass
        i+=1
    product_number_search_bar.send_keys(Keys.ENTER)

    sleep(randint(2,3))

    detect_capcha()

    for i in range(len(serial_numbers)):
        product_detail = driver.find_element_by_id(f"details_link_{serial_numbers[i]}")
        product_detail_link = product_detail.find_element_by_link_text("Afficher les détails")
        product_detail_link.click()

        # Log into file each pruct scrapped
        # DEBUG
        print(i)
        
        sleep(2)
        back_to_menu = driver.find_element_by_xpath("//*[@id='body']/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div[2]/input")
        back_to_menu.click()
        i += 1


# hp_warrenty_check()

def test():
    data = get_web_data()["hp"]["data"]
    serial_numbers = []
    product_numbers = []
    for i in data:
        serial_numbers.append(data[i]["serial_number"])
        product_numbers.append(data[i]["product_number"])
        i=+1

    print(len(serial_numbers))
    print(len(product_numbers))

    i = 0
    while i < len(serial_numbers):
        serial_numbers_batch = serial_numbers[i:i+20]
        i += 20

test()





def hp_part_surfer():
    driver.get(get_web_data()["hp"]["website"]["part_surfer"])

    sleep(randint(3,4))
    
    country_drop_down = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_ddlCountry")
    selected_country_drop_down = Select(country_drop_down)
    selected_country_drop_down.select_by_visible_text("France")
    serial_number_search_bar = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_SearchText_TextBox1")
    serial_number_search_bar.send_keys(get_web_data()["hp"]["data"]["0"]["serial_number"])
    serial_number_search_bar.send_keys(Keys.ENTER)


   
