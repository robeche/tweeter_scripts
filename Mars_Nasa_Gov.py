# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:52:29 2023

@author: rober
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import datetime as dt
from urllib.parse import urljoin
import os
from datetime import datetime


    
executable_path = {'executable_path': 'X:/chromedriver/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

base_url = 'https://mars.nasa.gov'
url = urljoin(base_url, 'news')

# Visit the mars nasa site
browser.visit(url)

# Get first list item and wait half a second if not immediately present
browser.is_element_present_by_css('ul.item_list li.slide', wait_time=0.5)

html = browser.html
news_soup = bs(html, 'html.parser')


#pandas file
base_path = 'X:/XPLOR/BuildHeightMap/WebScrappers'
file = 'Mars_Nasa2.pkl'
file_path = os.path.join(base_path,file)

if not os.path.isfile(file_path):
    df = pd.DataFrame(columns=['Date', 'Title', 'Link', 'Paragraph','Twitted'])
else:
    df = pd.read_pickle(file_path)
    
    
try:
    slide_element = news_soup.select('ul.item_list li.slide')

    for element in slide_element:
        # User the parent element to find the first <a> tag and save it as news_title
        news_title = element.find('div', class_='content_title')
        
        news_link = [a['href'] for a in news_title.select('a[href]')][0]
        
        news_link = urljoin(base_url, news_link)
        
        news_title=news_title.get_text()
    
        # Get the news paragraphs
        news_paragraph = element.find('div', class_='article_teaser_body').get_text()
        
        news_date = element.find('div', class_='list_date').get_text()
        
        time_obj = datetime.strptime(news_date, "%B %d, %Y")
        
        new_row = pd.DataFrame({'Date':[time_obj],'Title':[news_title],'Link':[news_link],'Paragraph':[news_paragraph],'Twitted':False})
        
        df = pd.concat([df,new_row], ignore_index=True)
except AttributeError:
    print('There was an error')
    

df.to_pickle(file_path)

    
    

