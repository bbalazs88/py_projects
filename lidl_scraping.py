from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.lidl.hu/hu/index.htm')
html = html.content
soup = BeautifulSoup(html, 'html.parser')

subtitle = soup.find_all('span', {'class' : 'theme__subtitle'})
title = soup.find_all('span', {'class' : 'theme__title'})

akciok = []

for i, j in zip(title, subtitle):
    akciok.append(i.text.lower() + " -- " + j.text.lower())

if "amerik" in akciok:
    print('Amerikai hét lesz!')

elif "mexikó" in akciok:
    print('Mexikói hét lesz!')

else:
    print('Nem lesz semmi érdekes.')

print('\n')

for i in akciok:
    print(i)