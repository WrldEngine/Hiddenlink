# Pulatov Kamran(c)
import requests
from bs4 import BeautifulSoup
GREEN='\033[32m'
RED='\033[31m'
banner = '''

██╗░░██╗██╗██████╗░██████╗░███████╗███╗░░██╗  ██╗░░░░░██╗███╗░░██╗██╗░░██╗
██║░░██║██║██╔══██╗██╔══██╗██╔════╝████╗░██║  ██║░░░░░██║████╗░██║██║░██╔╝
███████║██║██║░░██║██║░░██║█████╗░░██╔██╗██║  ██║░░░░░██║██╔██╗██║█████═╝░
██╔══██║██║██║░░██║██║░░██║██╔══╝░░██║╚████║  ██║░░░░░██║██║╚████║██╔═██╗░
██║░░██║██║██████╔╝██████╔╝███████╗██║░╚███║  ███████╗██║██║░╚███║██║░╚██╗
╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝  ╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
Author: Pulatov Kamran
Pulatov Kamran(C)
'''
print(RED + banner)
url = input(GREEN + "Enter a url: ")
HEADERS = {'user-agent': 'your user-agent'}
response = requests.get(url, headers=HEADERS)
bs = BeautifulSoup(response.content, 'html.parser')
for url in bs.find_all('a'):
    print(url.get('href'))
