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


def modify_xlsx(dict):

    df = pd.DataFrame(dict)
    # place array into df
    # Replace df

    df.to_excel('./data/data.xlsx', sheet_name='HP')






# df = pd.DataFrame({'serial_number':['CZJ029073S', 'CZJ029073T', 'ACM029T0XJ', 'CZ20290VD0'],
# 'brand':['HPE', 'HPE', 'HPE', 'HPE'],
# 'modele':['DL360 Gen10', 'DL360 Gen10', 'MSA 1050', 'StoreOnce 3620 24TB System'],
# 'product_number':['867959-B21', '867959-B21', 'Q2R21B', 'BB954A']
# })
# income1 = pd.DataFrame({'Names': ['Stephen', 'Camilla', 'Tom'],
#             'Salary':[100000, 70000, 60000]})

# income2 = pd.DataFrame({'Names': ['Pete', 'April', 'Marty'],
#                    'Salary':[120000, 110000, 50000]})

# income3 = pd.DataFrame({'Names': ['Victor', 'Victoria', 'Jennifer'],
#                    'Salary':[75000, 90000, 40000]})

# income_sheets = {'Group1': income1, 'Group2': income2, 'Group3': income3}
# writer = pd.ExcelWriter('./income.xlsx', engine='xlsxwriter')

# for sheet_name in income_sheets.keys():
#     income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

# writer.save()

# students_grades = pd.read_excel('./grades.xlsx', sheet_name='Grades', index_col='Grade')
# students_grades.head()