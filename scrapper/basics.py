# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:28:29 2021

@author: IT Help Desk
"""

from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))