'''Código para realizar a automação sem utilizar WebDriver'''

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import parametros

with requests.Session() as c:

    #Realiza o login
    c.get(parametros.url_login)
    page_login = c.post(parametros.url_login, data=parametros.data_login, headers=parametros.headers_login)
    print(page_login.text)
    cookies = c.cookies

    print("\n########### Fim da página de login ############\n")

    #Acessa a página inicial, não sei se é necessário
    c.get(parametros.url_main, cookies=cookies)
    page_main = c.post(parametros.url_main_post, data=parametros.data_main, headers=parametros.headers_main)

    #Acessa a página de circulação
    page_circ = c.get(parametros.url_circ, cookies=cookies, headers= parametros.headers_circ)
    soup = BeautifulSoup(page_circ.text, 'lxml')
    frames = soup.find(id="div_conteudo")
    frames = soup.find_all('span')
    print(soup)
    print("#### Primeiro livro da lista:  ")
    print(frames[46])
