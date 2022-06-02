from bs4 import BeautifulSoup as bs
import requests

url = "https://www.data-transitionnumerique.com/beautifulsoup-scraping/"
response = requests.get(url)
html = response.content

soup = bs(html, 'lxml')

# print(soup.prettify())
print(soup.title.get_text())
print(soup.a["href"])
print("test")
# titre_articles = soup.find_all(class_="card-title")
# print(titre_articles)
# for titre in titre_articles:
#     print(titre.get_text(strip=True))

import pandas as pd
categories = soup.find_all("h6", class_="category text-info")
categories_series = pd.Series(categories)
print(categories_series.value_counts())
