from bs4 import BeautifulSoup as bs
import requests
import time, random
from utils.json_loader import get_web_data

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

def get_hp():
    url = "https://support.hpe.com/hpsc/wc/public/find?rows%5B5%5D.item.countryCode=FR&rows%5B0%5D.item.countryCode=FR&rows%5B4%5D.item.serialNumber=&rows%5B4%5D.item.countryCode=FR&rows%5B8%5D.item.countryCode=FR&rows%5B8%5D.item.serialNumber=&rows%5B3%5D.item.countryCode=FR&rows%5B3%5D.item.serialNumber=&submitButton=Envoyer&rows%5B7%5D.item.countryCode=FR&rows%5B0%5D.item.serialNumber=CZJ029073S&rows%5B2%5D.item.countryCode=FR&rows%5B6%5D.item.countryCode=FR&rows%5B9%5D.item.countryCode=FR&rows%5B1%5D.item.serialNumber=&rows%5B7%5D.item.serialNumber=&rows%5B2%5D.item.serialNumber=&rows%5B5%5D.item.serialNumber=&rows%5B1%5D.item.countryCode=FR&rows%5B6%5D.item.serialNumber=&rows%5B9%5D.item.serialNumber="
    response = requests.get(url, headers=headers)
    html = response.content
    soup = bs(html, 'lxml')

    categories = soup.find_all("td")
    print(categories)


def get_dell():
    base_url = get_web_data()["dell"]["website"]["support"]
    num_serie = get_web_data()["dell"]["data"]["0"]["serial_number"]
    url = base_url + "/product-support/servicetag/" + num_serie + "/overview"
    # url = "https://www.dell.com/support/home/fr-fr/product-support/servicetag/0-Y2s4UDAveThoa1I4Y2RxQkt2clRSUT090/overview"
    print(url)

    response = requests.get(url, headers=headers)
    html = response.content
    soup = bs(html, 'lxml')

    print(soup.prettify().encode("utf-8"))
    # product = soup.find_all(class_="service-tag")
    # print(product)
    time.sleep(random.randint(1, 3))

get_dell()