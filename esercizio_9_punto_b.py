import json
from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
interessi_list = soup.select("#interessi .lista li")
list = []
for interessi in interessi_list:
    list.append(interessi.get_text())
 
list_json = json.dumps(list, indent = 2)

file = open("interessi.json", "w")
file.write(list_json)
file.close()

