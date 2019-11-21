from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml' )

for article in soup.find_all('article', class_='type-post'):
    title = article.header.h2.a.text
    print(title)
    
    descrip = article.div.p.text 
    print(descrip)
    
    divlink = article.find('div').text
    print(divlink)



