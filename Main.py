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
    trs = soup.find("table", { "class" : "tab_circulacoes max_width" }).findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        for td in tds:
            print( td.text )


