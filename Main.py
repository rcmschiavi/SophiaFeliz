#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import json

with requests.Session() as c:

    # Carrega os arquivos json
    with open( 'login.json' ) as data_file:
        data_login = json.load(data_file)

    with open( 'urls.json' ) as data_file:
        data_urls = json.load(data_file)

    # Realiza o login
    page_login = c.post(data_urls['login'], data=data_login)

    # Acessa a página de Circulações
    page_circ = c.get(data_urls['circ'])

    # Imprime as Circulações
    soup = BeautifulSoup(page_circ.text, 'lxml')
    frames = soup.find(id="div_conteudo")
    frames = soup.find_all('span')
    #print(soup)
    print("#### Primeiro livro da lista:  ")
    print(frames[46])
