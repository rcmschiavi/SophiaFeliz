#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json
import unicodedata

livros, prazos, usuario, id_livros, data_urls, data_params = [], [], "", [], json, json
c = requests.Session()

# Função com os procedimentos de login
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
    except Exception as e:
        print("Erro no login: ", e)
        exit(-1)

# Função com os procedimentos de acesso às circulações
def circ_op():
    global data_urls, livros, prazos, id_livros

    # Acessa a página de Circulações
    params_circ = {"content": "circulacoes"}
    page_circ = c.get(data_urls['index'], params=params_circ)

    # Captura as Circulações
    soup = BeautifulSoup(page_circ.content.decode('utf-8'), 'lxml')
    try:
        trs = soup.find("table", {"class": "tab_circulacoes max_width"}).findAll("tr")
        for tr in trs[1:]: # ignora a primeira linha da tabela
            tds = tr.findAll("td")
            livros.append( unicodedata.normalize("NFKC", tds[2].text) )
            prazos.append(tds[7].text)
            for td in tds:
                inps = td.findAll('input')
                for inp in inps:
                    id_livros.append(inp.get('value'))

    except Exception as e:
        print("Erro na circulação: ", e)
        exit(-1)

# Função que realiza as operações de renovação
def renovacao(livros_renov):
    try:
        #Define a variavel como o retorno da função de json
        str_livros_renov = json_renov(livros_renov)
        params_renov = {"num_circulacao": str_livros_renov}
        params_circ = {"content": "circulacoes"}
        params_renov.update(params_circ)

        # Faz o get enviando o parametro dos livros selecionados no url, no json do urls de renovação tem um {0}
        #que possibilita a concatenação dos livros a serem renovados
        page_renov = c.get(data_urls['index'], params=params_renov);

        #print(page_renov.url)

        # Retira os resultados da resposta
        soup_renov = BeautifulSoup(page_renov.content.decode('utf-8'), 'lxml')
        trs = soup_renov.findAll("td", {"class": "td_tabelas_valor2 esquerda"})
        num_livros =int(len(trs)/2 - 1)
        for i in range(0,num_livros,1):
            print(trs[3+i*2].text)

    except Exception as e:
        print("Erro na renovação: ", e)
        exit(-1)

# Função que gera o json final para renovação, atualmente gera uma string
def json_renov(livros_renov):
    lista = []

    # Formata os indices de livros que serão renovados em indices para o get
    for i, itens in enumerate(livros_renov):
        if (itens):
            lista.append(id_livros[i])

    str_livros_renov = ','.join(m for m in lista)

    return str_livros_renov
