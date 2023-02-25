#!/usr/bin/env python3

# Si no los tenemos instalamos BeautifulSoup y requests
# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests
import sys
import webbrowser # esta instalado por defecto, nos lleva a una pagina web desde python.

URL = "https://www.quefondos.com/es/fondos/ficha/index.html?isin=ES0164853014"
page = requests.get(URL)
# Lo que nos interesa de la pagina es el contenido por lo que usamos page.content
# y luego que lo pase en formato html
soup = BeautifulSoup(page.content, 'html.parser')
# Para la busqueda se pasa la etiqueta html en la que esta contenido el dato
# result = soup.find_all('span', class_="floatright")
result = soup.find_all('div', class_="w100")

valores = {}
for i in result:
    # getText() - elimina todas las etiquetas html y nos deja solo el contenido de texto.
    # find() - busca la primera conformidad con el parametro buscado.
    # print(i.getText())
    key = i.find('h4', id="bodytitle_h3_3")
    if key is not None:
        titulo = i.find('h4', id="bodytitle_h3_3")
        valor = i.find('span', class_='floatright')
        print(titulo)
        print(valor)
        print(f"{titulo.getText()}: {valor.getText()}")
    print("------------------------------------------------------")

# Nos muestra la página web que le pasemos la url.
webbrowser.open(URL)