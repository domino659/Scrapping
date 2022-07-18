from random import randint
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException


from variable import PATH_CHROMEDRIVER
from utils.json_loader import get_web_data

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}


# def scrapping_dell():
#     base_url = get_web_data()["dell"]["website"]["support"]
#     num_serie = get_web_data()["dell"]["data"]["0"]["serial_number"]
#     url = base_url + "/product-support/servicetag/" + num_serie + "/overview"
#     # url = "https://www.dell.com/support/home/fr-fr/product-support/servicetag/0-Y2s4UDAveThoa1I4Y2RxQkt2clRSUT090/overview"
#     print(url)

#     response = requests.get(url, headers=headers)
#     html = response.content
#     soup = bs(html, 'lxml')

#     print(soup.prettify().encode("utf-8"))
#     # product = soup.find_all(class_="service-tag")
#     # print(product)
#     time.sleep(random.randint(1, 3))


def scrapping_dell():
    options = Options()
    userAgent = UserAgent().random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(executable_path=PATH_CHROMEDRIVER)
    wait = WebDriverWait(driver, 20)

    driver.get(get_web_data()["dell"]["website"]["support"])
    sleep(randint(1, 3))
    num_serie = get_web_data()["dell"]["data"]["0"]["serial_number"]

    driver.get(f"https://www.dell.com/support/home/fr-fr/product-support/servicetag/{num_serie}/overview"
               )
    sleep(randint(1, 3))

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='top']/div[2]/div[2]/a[1]")))
    cookie = driver.find_element_by_xpath("//*[@id='top']/div[2]/div[2]/a[1]")
    cookie.click()

    product_number_search_bar = driver.find_element_by_id("inpEntrySelection")
    wait.until(EC.element_to_be_clickable((By.ID, "inpEntrySelection")))
    product_number_search_bar.send_keys(num_serie)
    product_number_search_bar.send_keys(Keys.ENTER)

    try:
        overlay = driver.find_element_by_id("sec-overlay")
        if overlay:
            print("I am Waiting")
            sleep(30)
            product_number_search_bar.send_keys(Keys.ENTER)
    except NoSuchElementException:
        pass

    wait.until(EC.element_to_be_clickable((By.ID, "viewDetailsRedesign")))
    product_detail = driver.find_element_by_id("viewDetailsRedesign")
    product_detail.send_keys(Keys.ENTER)
    sleep(10)
    # TODO Dode enquete de satisfaction
    # detect element if exist dodge

    wait.until(EC.element_to_be_clickable((By.ID, "warranty-cancel")))
    quit_product_detail = driver.find_element_by_id("warranty-cancel")
    quit_product_detail.click()
    sleep(10)
    wait.until(EC.element_to_be_clickable((By.ID, "changeproduct-mb")))
    change_product = driver.find_element_by_id("changeproduct-mb")
    change_product.click()
    # changeproduct for large screen
    sleep(200)

    driver.quit()


# https: // www.dell.com/support/home/fr-fr/product-support/servicetag/49YHBX2/overview
# /support/*/fr-fr
