import os
import pandas as pd
from pathlib import Path
from collections import defaultdict


from utils.text_modifier import array_to_nested_dict, delete_useless_info
from utils.log import *


CUR_DIR = Path(__file__).parent.parent


def find_dir(file_name):
    file = os.path.join(CUR_DIR, "data", f"{file_name}")
    return file


def open_xlsx(file_name):
    # Read xlsx document
    df = pd.read_excel(find_dir(file_name), engine='openpyxl')
    dict = df.to_dict()
    if df.empty:
        logging.info("File is empty.")
        exit("File is empty.")

    # Delete unecessary column
    dict.pop("Unnamed: 0")
    return dict


def modify_xlsx(contrat, garantie, number_index, file_name):
    filtred_garantie = delete_useless_info(garantie)
    contrat_dict = array_to_nested_dict(contrat, number_index)
    garantie_dict = array_to_nested_dict(filtred_garantie, number_index)
    data = open_xlsx(find_dir(file_name))
    dd = defaultdict(dict)

    # Regroup the 3 dicts
    for data in (data, contrat_dict, garantie_dict):
        for key, value in data.items():
            dd[key].update(value)

    # Convert it into a dataframe
    df = pd.DataFrame(dd)

    # Write it on the xlsx dociment
    writer = pd.ExcelWriter(find_dir(file_name), engine='xlsxwriter')
    df.to_excel(writer, sheet_name='HP')
    writer.save()
