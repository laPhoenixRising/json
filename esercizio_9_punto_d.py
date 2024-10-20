import json
import requests
from bs4 import BeautifulSoup

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')

link = soup.select("#link .lista li a")
link = link[0].get_text()
primo_link = str(link)

interessi = soup.select("#interessi .lista li")
interesse = interessi[0].get_text() 
primo_interesse = str(interesse)

citazioni = soup.select("#citazioni p")
citazione = citazioni[0].get_text()
prima_citazione = str(citazione)

dict = {"primo_link": primo_link, "primo_interesse": primo_interesse, "prima_citazione": prima_citazione} 

list_json = json.dumps(dict, indent = 2)

file = open("lista.json", "w")
file.write(list_json)
file.close()