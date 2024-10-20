import json
from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
citazioni_list = soup.select("p")
list = []
for citazioni in citazioni_list:
    list.append(citazioni.get_text())
 
list_json = json.dumps(list, indent = 2)

file = open("citazioni.json", "w")
file.write(list_json)
file.close()


