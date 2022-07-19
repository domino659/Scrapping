import http.client
import json

from variable import NETAPP_REFRESH_TOKENS
from utils.xlsx_manager import open_xlsx, modify_xlsx

conn = http.client.HTTPSConnection("api.activeiq.netapp.com")

file_name = "data_netapp.xlsx"


def generate_token():
    payload = "{\"refresh_token\":\"" + NETAPP_REFRESH_TOKENS + "\"}"
    headers = {
        'content-type': "application/json",
        'accept': "application/json"
    }
    conn.request("POST", "/v1/tokens/accessToken", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    return data["access_token"]


def fetch_data_api_netapp():
    data = open_xlsx(file_name)
    serial_numbers = list(data["serial_number"].values())
    print(serial_numbers)
    # token = generate_token()
    # print(token)
    # serial_number = "200000381553,200000381541"
    # headers = {
    #     'accept': "application/json",
    #     'authorizationtoken': token
    # }

    # conn.request(
    #     "GET", f"//v2/system/details/level/serial_numbers/id/{serial_number}", headers=headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))
