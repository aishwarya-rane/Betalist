import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://betalist.com/markets/finance-technology?page="

results = requests.get(url)
soup = BeautifulSoup(results.text , "html.parser")

print(soup)