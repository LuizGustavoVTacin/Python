from bs4 import BeautifulSoup
import requests

website = requests.get('https://www.kabum.com.br/produto/484852/placa-de-video-rtx-4070-nb-ex-v-colorful-geforce-nvidia-12gb-gddr6x')
content = website.text
soup = BeautifulSoup(content, 'html.parser')
box = soup.find('div', class_='sc-be35ab0-3.ifIPBx').get_text(strip= True, separator= ' ')
# title = soup.find('div',class_="jss276")
print(box)

#blocoValores > div.