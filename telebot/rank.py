# -*- coding: utf-8 -*-
import wget
import re
import requests
import os
import time
from bs4 import BeautifulSoup
while True:
    url = 'https://itunes.apple.com/cn/rss/toppodcasts/limit=100/genre=1318/xml'
    file = wget.download(url, bar=None)
    markup = open('xml', 'r')
    soup = BeautifulSoup(markup, "xml")

# print(soup.prettify())
    cell = soup.find_all('im:name')
    print cell;
    # td = cell.find_parents("entry")[0];
    indicator = True;
    counter = 0;
    for item in cell:
        if item.contents[0].find('TechFusion') != -1:
             print item.contents[0];
             counter += 1;
             print 'nahhhasdfsadfasdf'
             break;
        else: 
            print item.contents[0];
            counter += 1
    r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=TechFusion%20is%20now%20at%20%23"+ str(counter) +"%20place%20on%20iTunes%20Technology.&chat_id=-1001126950310")
    print(r.status_code, r.reason)
    os.remove("xml")
    time.sleep(600)