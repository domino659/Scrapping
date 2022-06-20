import os
import pandas as pd
from pathlib import Path

CUR_DIR = Path(__file__).parent.parent
DATA_FILE = os.path.join(CUR_DIR, "data", "data.xlsx")


def open_xlsx():
    df = pd.read_excel(DATA_FILE, engine='openpyxl')
    print(df)
    dict = df.to_dict()
    # Delete unecessary column
    dict.pop("Unnamed: 0")
    print(dict)
    return dict


def modify_xlsx():
    array = open_xlsx()
    # place array into df
    # Replace df
    df = pd.DataFrame({'serial_number': ['CZJ029073S', 'CZJ029073T', 'ACM029T0XJ', 'CZ20290VD0'],
                       'brand': ['HPE', 'HPE', 'HPE', 'HPE'],
                       'modele': ['DL360 Gen10', 'DL360 Gen10', 'MSA 1050', 'StoreOnce 3620 24TB System'],
                       'product_number': ['867959-B21', '867959-B21', 'Q2R21B', 'BB954A']
                       })
    # Chose wich page to replace
    df.to_excel('./data/data.xlsx', sheet_name='HP_Test')


def write_xlsx(data):
    array = open_xlsx()
    # place array into df
    # Replace df
    df = pd.DataFrame(data)
    # Chose wich page to replace
    df.to_excel('./data/data_test.xlsx', sheet_name='HP_Test')
