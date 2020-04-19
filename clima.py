import requests
from bs4 import BeautifulSoup

URL = 'https://weather.com/es-AR/tiempo/hoy/l/ARBA0009:1:AR'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')   

clima = soup.find(id='dp0-details-narrative').get_text()
print(clima)
