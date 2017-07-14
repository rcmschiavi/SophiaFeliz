#!/usr/bin/python
# -*- coding: utf-8 -*-

import Scraping
import re
import getpass


def input_login():
    """ Função para simular o recebimento de dados do chatBot """

    livros_renovar = []

    #Captura as informações de login que serão recebidas do chat
    matricula = input('Digite a matrícula (somente os numeros):\n')

    #Usando expressões regulares para ter certeza que o usuário inseriu
    # a matricula no formato correto
    r = re.compile('\d{10}')
    matricula = r.findall(matricula)
    #Repete a aquisição da matricula até que o usuario insira no formato correto
    while (len(matricula) < 1):
        matricula = input('A matrícula não está no formato correto (xxxxxxxxxx) :/\n'
                          'Digite ela novamente, por favor:\n')
        matricula = r.findall(matricula)

    # Pede senha após a matrícula estar correta.
    senha = getpass.getpass('Digite a senha:')
    print('Tentando login...')

    # Pegando somente o primeiro match da lista gerada no regex
    matricula = matricula[0]

    # Chama a função de login do scraping para poder obter os dados do
    #usuario e os livros que podem ser renovados
    Scraping.login(matricula, senha)

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
