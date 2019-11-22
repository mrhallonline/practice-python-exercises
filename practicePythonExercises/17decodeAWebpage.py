# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'http://jamaica-gleaner.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, "html5lib")

print(soup.prettify())