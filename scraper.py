import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/Sony-Systemkamera-Klapp-Display-Echtzeit-Autofokus-AF-Punkten/dp/B07MW8GTYD/ref=sr_1_16?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+camera&qid=1563301687&s=gateway&sr=8-16"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[:5])

    print(converted_price)
    print(title.strip())


check_price()
