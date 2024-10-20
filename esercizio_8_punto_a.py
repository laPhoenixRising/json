from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')
citazioni = soup.select("#citazioni p")
citazioni_string = str(citazioni)
file = open("citazioni.html", "w")
file.write(citazioni_string)
file.close()