"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup

# 發送GET請求並獲取網頁內容
url = 'https://mochat.tw/chat/vhdsCuBE9JJvjvRABpFg'
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML內容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到使用者留言的區塊
messages_section = soup.find(class_='jss276')

# 找到所有使用者留言的元素
messages = messages_section.find_all(class_='jss276')

# 輸出所有使用者留言
for message in messages:
    print(message.text)

