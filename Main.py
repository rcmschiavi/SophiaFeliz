#!/usr/bin/python
# -*- coding: utf-8 -*-

import Scraping
import Manager_DB
import ChatBot
import re


def input_login():
    """ Função para simular o recebimento de dados do chatBot """

    livros_renovar = []

    # Captura o id do usuario do facebook
    id_face = ChatBot.get_face()

    # Abre o DB para realizar as operações
    Manager_DB.abrir_db()

    # Define a variável com uma lista dos matchs de id_face com os registros do DB
    dados_db = Manager_DB.select(id_face)

    # Verifica se o id_facebook já está registrado, else faz o registro
    if (dados_db == []):
        print("Ainda não tenho sua matricula e senha.")
        matricula, senha = ChatBot.get_credenciais()
        Manager_DB.insert_cred(id_face,matricula,senha)
        dados_db = Manager_DB.select(id_face)
    else:
        matricula, senha = dados_db[0][2], dados_db[0][3]
        print("Já tenho suas credenciais.")
    print("Matrícula: {0} Senha1: {1}".format(matricula,senha))

    # Fecha o DB
    Manager_DB.conn.close()

    # Exit para realizar os testes sem fazer nenhum scraping
    exit(0)

    print('Tentando login...')

    # Chama a função de login do scraping para poder obter os dados do
    #usuario e os livros que podem ser renovados
    Scraping.login(matricula, senha)


    Manager_DB.select()

    # Usa regex para pegar somente o primeiro nome do usuário
    r = re.compile('\w+')
    print("Olá, {0}".format(r.findall(Scraping.usuario)[0].capitalize()))

    # Exibe os livros com as datas de vencimento
    print("Você tem os seguintes livros com as respectivas datas de vencimento:")
    for i in Scraping.livros:
        print("id: {0}  livro: {1}  vencimento: {2}".format(Scraping.livros.index(i)+1,i,Scraping.prazos[Scraping.livros.index(i)]))

    # Recebe a string dos livros que devem ser renovados, sem necessidade de formatação
    input_livros_renov = input('Digite o id dos livros que você deseja renovar: ')

    # Converte o valor recebido no input para uma lista de boolean mais para a renovação
    for i in Scraping.livros:
        # Verifica se existe algum valor no input com um find e um index no 'scraping.livros' procurando o valor atual de 'i'
        # Talvez exista alguma sintaxe mais adequada pra substituir esse 'index'
        livros_renovar.append(input_livros_renov.find(str(Scraping.livros.index(i)+1))!=-1)

    # Chama a função de renovação do scraping
    Scraping.renovacao(livros_renovar)

    # Informa a resposta da renovação para o usuário
    for i in Scraping.renov_livros:
        #Mesma indexação utilizada na verificação do input de renovação
        print("livro: {0} resultado: {1}".format(i,Scraping.renov_status[Scraping.renov_livros.index(i)]))


# Chama a função para realizar os inputs pelo usuario
input_login()
