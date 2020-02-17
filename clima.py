import requests
from bs4 import BeautifulSoup

URL = 'https://articulo.mercadolibre.com.ar/MLA-816680025-monitor-gamer-ultrawide-ips-25-pulg-lg-25um58-p-fullhd-cuota-_JM?quantity=1&variation=45349051022'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(id='productInfo').get_text()

price = price.split('$')[1][0:8]
price = float(price)
if price > 20.000:
    print(price)