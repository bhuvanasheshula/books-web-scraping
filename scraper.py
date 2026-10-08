import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
data = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"   # fixes the £ symbol showing as Â£

    if response.status_code != 200:
        print(f"Skipping page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        data.append({
            "Title": book.h3.a["title"],
            "Price": book.find("p", class_="price_color").text,
            "Rating": book.find("p", class_="star-rating")["class"][1],
            "Availability": book.find("p", class_="instock availability").text.strip(),
            "Link": "https://books.toscrape.com/catalogue/" + book.h3.a["href"]
        })

    print(f"Page {page} done - total books: {len(data)}")
    time.sleep(0.5)   # be polite to the website

df = pd.DataFrame(data)
df.to_csv("books_raw.csv", index=False)
print("Scraping completed! Total books:", len(df))