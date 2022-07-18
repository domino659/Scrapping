from scrapping.scrapping_hp import scrapping_hp
from scrapping.scrapping_dell import scrapping_dell
from api.netapp import fetch_data_api_netapp

if __name__ == '__main__':
    # scrapping_hp()
    # scrapping_dell()
    fetch_data_api_netapp()
