from bs4 import BeautifulSoup as bs
import html


def table_scrap(content):
    print("TRAVELLING")
    print(content)
    import unicodedata
    content = unicodedata.normalize('NFD', str(content)).encode(
        'ascii', 'ignore').decode("utf-8")
    print("UNIDECOD")
    print(content)

    soup = bs((content), 'lxml')
    print("THIS IS THE SOUP")
    print(type(soup))
    print(soup)
    table = []
    rows = soup.find_all('tr')
    for row in rows:
        table_row = []
        columns = row.find_all('td')
        for column in columns:
            table_row.append(column.get_text())
        table.append(table_row)
    return table
