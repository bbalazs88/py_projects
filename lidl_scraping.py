from bs4 import BeautifulSoup
import requests
import smtplib, ssl

'''
2019-03-10:
Elvileg az smtplib-el nem tudunk utf-8-as karaktereket kuldeni, tehat
az osszes ekezet kilove, ezert leegyszerusitettem az email kuldest arra,
hogy vagy lesz szamomra erdekes het, vagy nem.

Windows Task Schedulerben ütemezve minden péntekre, lidl_scraping nev alatt.
A lenyeg az volt, hogy megadni a python.exe elereset, 
illetve a py fajl elereset.

Csintaltam egy uj gmail fiokot, alabb a belepesi adatok. Kulon be kellett
allitani a nem biztonsagos belepest, vagy csokkentett biztonsagu belepest, 
valami ilyesmi. Emiatt kellett az uj account.

A bé mappabol ki kellett hoznom magat a fajlt, mert meghalt az smtplib az
ekezetre. A python.exe-et is a datasrev konyvtarban levo PyCharmProjects
mappabol futtatja.s

TODO:
A subject mezo tolteset lehetne meg megnezni, illetve az utf-8at tovabb
nyomozni
'''

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email =  # Enter your address
receiver_email = "baloghbalazs646@gmail.com"  # Enter receiver address
password = # Enter password

context = ssl.create_default_context()

html = requests.get('https://www.lidl.hu/hu/index.htm')
html = html.content
soup = BeautifulSoup(html, 'html.parser')

subtitle = soup.find_all('span', {'class' : 'theme__subtitle'})
title = soup.find_all('span', {'class' : 'theme__title'})

akciok = []
hit = ""
lidl_week = ""

for i, j in zip(title, subtitle):
    akciok.append(i.text.lower() + " -- " + j.text.lower())

if "amerik" in akciok:
    hit = 'Amerikai het lesz!'

elif "mexikó" in akciok:
    hit ='Mexikoi het lesz!'

else:
    hit = 'Nem lesz semmi erdekes.'

for i in akciok:
    lidl_week = lidl_week + i + "\r\n"

lidl_week = (hit + "\r\r\n" + lidl_week)

# print(lidl_week)
# print(hit)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, hit)
    server.quit()
