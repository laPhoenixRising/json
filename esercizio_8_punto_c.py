from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
interessi = soup.select("#interessi .lista li")
ultimo_interesse = interessi[3] 
ultimo_interesse_string = str(ultimo_interesse)
file = open("interessi.html", "w")
file.write(ultimo_interesse_string)
file.close()