# -*- coding: utf-8 -*-
import wget
import re
import requests
import os
import time
from bs4 import BeautifulSoup
while True:
    url = 'https://podcast.okihika.com/CN/1318'
    file = wget.download(url, bar=None)
    html = open('1318', 'r')
    soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
    cell = soup.find(href = "/CN/iid/1202658654/%E7%A7%91%E6%8A%80%E8%81%9A%E5%8F%98%20(TechFusion)")
    td = cell.find_parents("td")[0]
    string = td.span.prettify()
    string = string.splitlines()[1]
    string = re.sub("\D", "", string)
    print string
    r = requests.get("https://api.telegram.org/bot370638413:AAHrBMWdw1QzNP6LJ2HBZqfhbrislpOv_4g/sendMessage?text=TechFusion%20is%20now%20at%20%23"+ string +"%20place%20on%20iTunes%20Technology.&chat_id=-1001126950310")
    print(r.status_code, r.reason)
    os.remove("1318")
    time.sleep(600)

