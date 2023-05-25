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

base_url = 'https://www.esa.int/'
url = urljoin(base_url, 'Science_Exploration/Human_and_Robotic_Exploration')

# Visit the mars nasa site
browser.visit(url)

# Get first list item and wait half a second if not immediately present
browser.is_element_present_by_css('ul.item_list li.slide', wait_time=0.5)

html = browser.html
news_soup = bs(html, 'html.parser')

#pandas file
base_path = 'X:/XPLOR/BuildHeightMap/WebScrappers'
file = 'ESA.pkl'
file_path = os.path.join(base_path,file)

if not os.path.isfile(file_path):
    df = pd.DataFrame(columns=['Type','Date', 'Title', 'Link', 'Paragraph','Twitted'])
else:
    df = pd.read_pickle(file_path)
    
    
try:
    slide_element = news_soup.select('section.filtered div.clearfix div.grid-item')

    for element in slide_element:
        # User the parent element to find the first <a> tag and save it as news_title
        if "Story" in element.get_text():
            type = "story"
            
            news_title = element.find('h3', class_='heading').get_text()
            
            news_link = [a['href'] for a in element.select('a[href]')][0]
            
            news_link = urljoin(base_url, news_link)
            
            news_date = element.find('div', class_='meta').select_one('span').get_text()
                   
            time_obj = datetime.strptime(news_date, "%d/%m/%Y")

            
            # Get the news paragraphs
            browser.visit(news_link)
            html_news = browser.html
            news_soup = bs(html_news, 'html.parser')
            
            abstract = news_soup.select_one('div.abstract')
            
            if abstract:
                abstract=abstract.select_one('p').get_text()
                news_paragraph=abstract
            else:
                news_paragraph = news_soup.select_one('div.c-summary__body').select_one('p').get_text()

            
            new_row = pd.DataFrame({'Type':[type],'Date':[time_obj],'Title':['#ESA ' + news_title],'Link':[news_link],'Paragraph':[news_paragraph],'Twitted':False})
            
            df = pd.concat([df,new_row], ignore_index=True)
            
            
        elif "Image" in element.get_text():
            type = "image"
            
            news_title = element.find('h3', class_='heading').get_text()
            
            news_link = [a['href'] for a in element.select('a[href]')][0]
            
            news_link = urljoin(base_url, news_link)
            
            news_date = element.find('div', class_='meta').select_one('span').get_text()
                   
            time_obj = datetime.strptime(news_date, "%d/%m/%Y")

            
            # Get the news paragraphs
            browser.visit(news_link)
            html_news = browser.html
            news_soup = bs(html_news, 'html.parser')
            
            news_paragraph = news_soup.select_one('div.modal__tab-description').select_one('p').get_text()
            new_row = pd.DataFrame({'Type':[type],'Date':[time_obj],'Title':['#ESA ' + news_title],'Link':[news_link],'Paragraph':[news_paragraph],'Twitted':False})
            
            df = pd.concat([df,new_row], ignore_index=True)

            
        elif "Video" in element.get_text():
            type = "video"
            news_title = element.find('h3', class_='heading').get_text()
            news_link = [a['href'] for a in element.select('a[href]')][0]
            
            news_link = urljoin(base_url, news_link)
            
            news_date = element.find('div', class_='meta').select_one('span').get_text()
                   
            time_obj = datetime.strptime(news_date, "%d/%m/%Y")

            
            # Get the news paragraphs
            browser.visit(news_link)
            html_news = browser.html
            news_soup = bs(html_news, 'html.parser')
            
            news_paragraph = news_soup.select_one('div.modal__tab-description').select_one('p').get_text()
            new_row = pd.DataFrame({'Type':[type],'Date':[time_obj],'Title':['#ESA ' + news_title],'Link':[news_link],'Paragraph':[news_paragraph],'Twitted':False})
            
            df = pd.concat([df,new_row], ignore_index=True)
        else:
            pass
            
            
        
        
        
except AttributeError:
    print('There was an error')
    

df.to_pickle(file_path)
 