#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json

livros, prazos, usuario, data_urls, data_params = [], [], "", json, json
c = requests.Session()

#Função com os procedimentos de login
def login():
    global usuario, c, data_params, data_urls
    # Carrega os arquivos json
    with open( 'params.json' ) as data_file:
        data_params = json.load(data_file)

    with open( 'urls.json' ) as data_file:
        data_urls = json.load(data_file)

    # Realiza o login
    page_login = c.post(data_urls['login'], data=data_params['login'])
    soup_login = BeautifulSoup(page_login.text, 'lxml')
    try:
        result_login = soup_login.find("table").find("b")
        usuario = result_login.text
        circ_op()
    except: print("Erro no login")

#Função com os procedimentos de acesso às circulações
def circ_op():
    global data_urls, livros, prazos

    # Acessa a página de Circulações
    page_circ = c.get(data_urls['circ'])

    # Imprime as Circulações
    soup = BeautifulSoup(page_circ.content.decode('utf-8'), 'lxml')
    try:
        trs = soup.find("table", {"class": "tab_circulacoes max_width"}).findAll("tr")
        for tr in trs:
            tds = tr.findAll("td")
            livros.append(tds[2].text)
            prazos.append(tds[7].text)
    except:
        print("Erro na circulação")

#Função que realiza as operações de renovação
def renovacao(livros_renov = []):
    lista = "num_circulacao : "
    i=0

    #Formata os indices de livros que serão renovados em indices para o get
    for itens in livros_renov:
        if(itens):
            lista+="71390{0}".format(i+1)
        i+=1

    print(lista)
    data_renov="{0}+{1}+{2}".format(data_params['renovacao_pt1'],lista,data_params['renovacao_pt2'])
    print(data_renov)
    page_renov = c.get(data_urls['renov'], data=data_renov)
    soup_renov = BeautifulSoup(page_renov.text, 'lxml')
    #Essa parte final ainda não está funcionando, para informar quais livros foram renovados com sucesso
    #As vezes não dá pra renovar pq alguém reservou
    trs = soup_renov.findAll("table", {"class": "tab_circulacoes max_width"}).findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        for td in tds:
    print(page_renov.text)