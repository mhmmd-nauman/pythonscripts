# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:12:30 2020

@author: Nauman
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
print ("Hello, Python!");
driver = webdriver.Chrome("chromedriver.exe")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.clarionlist.com/")
content = driver.page_source
soup = BeautifulSoup(content)
#for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
for a in soup.findAll('a',href=True):
    print(a.text)
    #name=a.find('div', attrs={'class':'_3wU53n'})
    #price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    #products.append(name.text)
    prices=""
    prices.append(a.text)
   # ratings.append(rating.text)
    #df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':"ss"})
    df = pd.DataFrame({'Link':prices})
    df.to_csv('link.csv', index=False, encoding='utf-8')