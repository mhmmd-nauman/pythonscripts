# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:42:55 2020

@author: Nauman
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.revzilla.com/faq")

wysiwyg__content = driver.find_elements_by_xpath('//*[@id="main-content"]/div[4]/div')
#text = wysiwyg__content.text
print(wysiwyg__content)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()