# Pulatov Kamran(c)
import requests
from bs4 import BeautifulSoup
url = input("Enter a url: ")
HEADERS = {'user-agent': 'your user-agent'}
response = requests.get(URL, headers=HEADERS)
bs = BeautifulSoup(response.content, 'html.parser')
for url in bs.find_all('a'):
    print(url.get('href'))
