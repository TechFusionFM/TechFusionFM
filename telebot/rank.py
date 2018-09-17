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

def my_function(url, genre):
    file = wget.download(url, out="myFile.xml")
    markup = open('myFile.xml', 'r')
    soup = BeautifulSoup(markup, "xml")
    cell = soup.find_all('im:name')
    print cell;
    indicator = True;
    counter = 0;
    uncharted = [0, 1, 2];
    unchartedString = ""
    for item in cell:
        print item.contents[0]
        if item.contents[0] == '聚焦 (《科技聚变》出品）':
            counter += 1;
            uncharted.remove(0)
            r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=《聚焦》is now at %23"+ str(counter) +" on Apple Podcasts " + genre + " Chart (Testing).&chat_id=-1001126950310")
            print(r.status_code, r.reason)
        elif item.contents[0] == '小玩意儿 (《科技聚变》出品）':
            counter += 1;
            uncharted.remove(1)
            r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=《小玩意儿》is now at %23"+ str(counter) +" on Apple Podcasts " + genre + " Chart (Testing).&chat_id=-1001126950310")
            print(r.status_code, r.reason)
        elif item.contents[0] == '科技聚变':
            counter += 1;
            uncharted.remove(2)
            r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=《科技聚变》is now at %23"+ str(counter) +" on Apple Podcasts " + genre + " Chart (Testing).&chat_id=-1001126950310")
            print(r.status_code, r.reason)
        else: 
            counter += 1
    
    for item in uncharted:
        unchartedString += str(item) + ""
    r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text="+ unchartedString +" not charting (Testing).&chat_id=-1001126950310")
    print(r.status_code, r.reason)
        
    os.remove("myFile.xml")    
    
# Keep looping for every 10 mins
while True:
    my_function("https://itunes.apple.com/cn/rss/toppodcasts/limit=200/genre=1318/xml", "Technology")
    my_function("https://itunes.apple.com/cn/rss/toppodcasts/limit=200/xml", "All Podcasts")
    time.sleep(600)
