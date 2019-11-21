from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml' )

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'link', 'iframe'])

for article in soup.find_all('article', class_='type-post'):
    title = article.header.h2.a.text
    print(title)
    
    descrip = article.div.p.text 
    print(descrip)
    
    try:
        divlink = article.find('figure').div.text
    except:
        divlink = "no divlink"
    print(divlink)
    
    try:
        vid_src = article.find('iframe')['src']
    except:
        vid_src = "No iframe found"
    print(vid_src)
    
    print()
    csv_writer.writerow([title,descrip,divlink, vid_src])

csv_file.close()