import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from money_parser import price_str
import send_email

load_dotenv()

SCRAPED_PAGE_URL = os.getenv("SCRAPED_PAGE_URL")

resp = requests.get(SCRAPED_PAGE_URL)
html = BeautifulSoup(resp.text, "html.parser")

phone_model = "Samsung S24"

def get_price():
  price_el = html.findChild("p", attrs={ 'class': "product-new-price" })

  return float(price_str(price_el.text))

def get_name():
  name_text = html.findChild("h1", attrs={ 'class': "page-title" }).text.strip()
  
  assert name_text.find(phone_model)
  return name_text


def get_rating():
  rating_text = html.findChild("a", attrs={ 'class': "rating-text" }).text.strip()

  score = rating_text.split(" ")[0]

  return score
  
def check_price():
  base_price = 6000
  
  if get_price() < base_price:
    print("Price went down - send email")
    send_email.send_price_alert_email(phone_model=phone_model, price=get_price(), rating=get_rating())
  else:
    print("Price is high")
  
check_price()
