import requests
from bs4 import BeautifulSoup
import re
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

sender = os.getenv("SENDER")
password = os.getenv("PASSWORD")

class Product:
    def __init__(self, name, size, price, url):
        self.name = name
        self.size = size
        self.price = price
        self.url = url


    def __str__(self):
        return "{} {} - ${} -- url: {}".format(self.name, self.size, self.price, self.url)
    
    def __repr__(self):
        return "{} {} - ${} -- url: {}".format(self.name, self.size, self.price, self.url)

url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

products: list[Product] = []
options = soup.find(name="ul", class_="a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-top-micro swatches swatchesSquare")
for option in options.findAll(name="li"):
    name = "Instant Pot"
    size = option.find(name="p", class_="a-text-left a-size-base").text.strip()
    price_full_text = option.find(name="p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice").text.strip()
    price_search = re.search(r"\$(\d+.\d+)", price_full_text)
    if price_search:
        price = float(price_search.group(1))
    final_product = Product(name, size, price, url)
    print(final_product)
    products.append(final_product)

def send_email(sender, receiver, password, subject, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=receiver, msg=f"Subject:{subject}\n\n{body}")
    

buying_price = 100
for product in products:
    if product.price < buying_price:
        email_subject = "{} {} < ${}".format(product.name, product.size, buying_price)
        email_body = "The {} {} is now ${}! Get it at {}".format(product.name, product.size, product.price, product.url)
        send_email(sender=sender, receiver=sender, password=password, subject=email_subject, body=email_body)
