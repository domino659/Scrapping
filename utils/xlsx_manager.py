import os
import pandas as pd
from pathlib import Path
from collections import defaultdict


from utils.text_modifier import array_to_nested_dict, delete_useless_info
from utils.log import *


CUR_DIR = Path(__file__).parent.parent
DATA_FILE = os.path.join(CUR_DIR, "data", "data.xlsx")


def open_xlsx():
    df = pd.read_excel(DATA_FILE, engine='openpyxl')
    dict = df.to_dict()
    if df.empty:
        logging.info("File is empty.")
        exit("File is empty.")

    # Delete unecessary column
    dict.pop("Unnamed: 0")
    return dict


def modify_xlsx(contrat, garantie, number_index):
    filtred_garantie = delete_useless_info(garantie)
    contrat_dict = array_to_nested_dict(contrat, number_index)
    garantie_dict = array_to_nested_dict(filtred_garantie, number_index)
    data = open_xlsx()
    dd = defaultdict(dict)

    for data in (data, contrat_dict, garantie_dict):
        for key, value in data.items():
            dd[key].update(value)

    df = pd.DataFrame(dd)
    df.to_excel('./data/data.xlsx', sheet_name='HP')
