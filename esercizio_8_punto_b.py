from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
interessi = soup.select("#interessi .lista li")
interessi_string = str(interessi)
file = open("interessi.html", "w")
file.write(interessi_string)
file.close()