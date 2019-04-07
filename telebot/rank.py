# -*- coding: utf-8 -*-
import sys  
import wget
import re
import requests
import os
import time
from bs4 import BeautifulSoup
reload(sys)  
sys.setdefaultencoding('utf8')

def my_function(url, genre, shows, uncharted):
    url = "https://itunes.apple.com/cn/rss/toppodcasts/limit=200/" + url 
    file = wget.download(url, out="myFile.tmp", bar=None)
    markup = open('myFile.tmp', 'r')
    soup = BeautifulSoup(markup, "xml")
    cell = soup.find_all('im:name')
    indicator = True;
    counter = 0;
    for item in cell:
        for show in shows:
            if item.contents[0] == show:
                counter += 1
                msg = ""
                msg += show
                msg += "\n %23"
                msg += str(counter) 
                msg += " on \n"
                msg += genre
                msg += " Chart."
                print msg
                r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=" + msg + "&chat_id=-1001126950310")
                print(r.status_code, r.reason)
        counter += 1
    os.remove("myFile.tmp")    
    
# Keep looping for every 10 mins
while True:
    my_function("xml", "All Podcasts", ['聚焦 (《科技聚变》出品）', '小玩意儿 (《科技聚变》出品）', '科技聚变'], [0, 1, 2])
    my_function("genre=1318/xml", "Technology", ['聚焦 (《科技聚变》出品）', '小玩意儿 (《科技聚变》出品）', '科技聚变'], [0, 1, 2])
    my_function("genre=1446/xml", "Gadgets", ['小玩意儿 (《科技聚变》出品）'], [0])
    my_function("genre=1448/xml", "Tech News", ['聚焦 (《科技聚变》出品）', '科技聚变'], [0, 1])
    time.sleep(600)

