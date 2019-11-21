# scrape Title,description, and link
# header(class=entry-header),h2,a,text
# description(div, class=entry-content),p

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml' )
#to find title
header = soup.find('header', class_='entry-header')
title = header.h2.a.text
#to find description
div = soup.find('div', class_='entry-content')
descrip = div.p.text 
#to find link to video
divlink = soup.find('div', class_='wp-block-embed_wrapper')
figure = soup.find('figure', class_='wp-block-embed')
link = figure.div.text

# description =

print(title)
print(descrip)
print(link)