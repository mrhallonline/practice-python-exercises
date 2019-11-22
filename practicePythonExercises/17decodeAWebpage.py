# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'http://jamaica-gleaner.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")


# print(titles)

for h2 in soup.find_all('h2'):
    try:
        titles = h2.a.text
    except:
         titles = 'no title found'
    print(titles)
    print('-------')

for h3 in soup.find_all('h3'):
    try:
        sub_titles = h3.a.text
    except:
        sub_titles = "no subtitles found"
    print(sub_titles)
    print('-------')