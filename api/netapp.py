import requests

from variable import NETAPP_API_KEY

headers = {'accept': 'application/json',
           'authorizationtoken': NETAPP_API_KEY}

url = "https://api.activeiq.netapp.com//"
request = "v2/system/details/level/customer/id/string"
complete_url = url + request


def generate_token():
    r = requests.get(complete_url, headers=headers)
    print(r.json())
    return r.json()['token']


def fetch_data_api_netapp():
    r = requests.get(complete_url, headers=headers)
    print(r.json())
