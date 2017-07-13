#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json

livros, prazos, usuario, id_livros, data_urls, data_params = [], [], "", [], json, json
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
    global data_urls, livros, prazos, id_livros

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
            for td in tds:
                inps = td.findAll('input')
                for inp in inps:
                    id_livros.append(inp.get('value'))

    except:
        print("Erro na circulação")

#Função que realiza as operações de renovação
def renovacao(livros_renov):
    try:
        #Define a variavel como o retorno da função de json
        data_renov, lista = json_renov(livros_renov)
        print(data_renov)

        #Faz o get enviando o parametro dos livros selecionados no url, no json do urls de renovação tem um {0}
        #que possibilita a concatenação dos livros a serem renovados
        page_renov = c.get(data_urls['renov'].format(lista))

        #Retira os resultados da resposta
        soup_renov = BeautifulSoup(page_renov.content.decode('utf-8'), 'lxml')
        trs = soup_renov.findAll("td", {"class": "td_tabelas_valor2 esquerda"})
        num_livros =int(len(trs)/2 - 1)
        for i in range(0,num_livros,1):
            print(trs[3+i*2].text)

    except: print("Erro na renovação")

#Função que gera o json final para renovação
def json_renov(livros_renov):
    json_id_renov = {}
    lista = []
    i = 0
    # Formata os indices de livros que serão renovados em indices para o get
    for itens in livros_renov:
        if (itens):
            lista.append(id_livros[i + 1])
        i += 1

    #remove os caracteres indesejáveis para o concatenar o json
    json_id_renov['num_circulacao'] = lista
    json_id_renov = json.dumps(json_id_renov)
    json_id_renov = json_id_renov.replace("{", "")
    json_id_renov = json_id_renov.replace("}", "")
    json_final_pt1 = json.dumps(data_params['renovacao_pt1']).replace("}", "")
    json_final_pt2 = json.dumps(data_params['renovacao_pt2']).replace("{", "")
    data_renov = "{0}, {1}, {2}".format(json_final_pt1, json_id_renov, json_final_pt2)
    lista = str(lista)
    lista = lista.replace("[","")
    lista = lista.replace("]","")
    lista = lista.replace("'","")
    lista = lista.replace(" ","")
    return data_renov, lista
