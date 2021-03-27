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
driver.get("https://www.amazon.com/s?k=laptops&page=1")
content = driver.page_source
soup = BeautifulSoup(content)
#for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col'}):
    name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
    price = d.find('span', attrs={'class':'a-offscreen'})
    rating = d.find('span', attrs={'class':'a-icon-alt'})
    if name is not None:
        products.append(name.text)
    if rating is not None:
        rating.append(rating.text)   
    
    #df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':"ss"})
df = pd.DataFrame({'Product Name':products})
df.to_csv('products.csv', index=False, encoding='utf-8')