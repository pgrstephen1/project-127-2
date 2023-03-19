from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge("C:/Whitehat_jr/PRO-127-130/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

star_data = []

headers = ["name", "distance", "mass", "radius"]


soup = BeautifulSoup(browser.page_source, "html.parser")
starTable = soup.find('table')
tableRows = starTable.find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_data.append(row)
Star_names = []
Distance = []
Mass = []
Radius = []


for i in range(1, len(star_data)):
    Star_names.append(star_data[i][1])
    Distance.append(star_data[i][3])
    Mass.append(star_data[i][5])
    Radius.append(star_data[i][6])

df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), 
columns=['Star_name', 'Distance', 'Mass', 'Radius']) 
print(df2) 
df2.to_csv('bright_stars.csv')
