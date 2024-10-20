from bs4 import BeautifulSoup
import requests

request = requests.get('https://laphoenixrising.github.io/')
html = request.text
soup = BeautifulSoup(html, 'html.parser')

link = soup.select("#link .lista li a")
primo_link = str(link[0])

interessi = soup.select("#interessi .lista li")
primo_interesse = str(interessi[0]) 

citazioni = soup.select("#citazioni p")
prima_citazione = str(citazioni[0])

contenuto = primo_link + "\n" + primo_interesse + "\n" + prima_citazione 

file = open("contenuto.html", "w")
file.write(contenuto)
file.close()