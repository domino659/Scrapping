import os, json
from pathlib import Path

CUR_DIR = Path(__file__).parent.parent
DATA_FILE = os.path.join(CUR_DIR, "data", "web_data.json")

def get_web_data():
    with open(DATA_FILE, "r") as f:
        web_data = json.load(f)
        # print(web_data)
    return web_data