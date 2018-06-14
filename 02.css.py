from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())

bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
bs.find_all('span', {'class': {'green', 'red'}})
nameList = bs.find_all(text='the prince')
print(len(nameList))

# keyword
title = bs.find_all(id='title', class_='text')      # id is unique
print(len(title))
title = bs.find_all(id='title')
print(len(title))
title = bs.find_all('', {'id': 'title'})
print(len(title))
