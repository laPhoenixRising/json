import json
from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
interessi = soup.select("#interessi .lista li")
ultimo_interesse = interessi[3].get_text() 
ultimo_interesse_string = str(ultimo_interesse)

dict = {"ultimo interesse": ultimo_interesse_string}

list_json = json.dumps(dict)

file = open("ultimo", "w")
file.write(list_json)
file.close()