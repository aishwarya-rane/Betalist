import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


company_name = []
description = []



default = "https://betalist.com/markets/finance-technology?page="
urls = [default]

for i in range(1,21):
  urls.append(default+str(i))


def companies(url):
  results = requests.get(url)
  soup = BeautifulSoup(results.text , "html.parser")
  company = soup.find_all('div', class_ ="startupCard")
  return company

def names(companies):
  for container in companies:
    name = container.find("a", class_="startupCard__details__name").text
    company_name.append(name)
  return company_name

def des(companies):
  for container in companies:
    des = container.find("a", class_ ="startupCard__details__pitch").text
    description.append(des)
  return description

for i in range(len(urls)):
  page = companies(urls[i])
  company_name = names(page)
  description = des(page)


companies = pd.DataFrame({
'name': company_name,
'description': description,
})

companies.to_csv('fintech.csv')





   


