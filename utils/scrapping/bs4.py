from bs4 import BeautifulSoup as bs

from utils.text_modifier import normalizer


def table_scrap(content):
    soup = bs((content), 'lxml')
    table = []
    rows = soup.find_all('tr')
    for row in rows:
        table_row = []
        columns = row.find_all('td')
        for column in columns:
            table_row.append(column.get_text())
        table.append(normalizer(table_row))
    return table
