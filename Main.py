#!/usr/bin/python
import Scraping
import json
import re



#Função para simular o recebimento de dados do chatBot
def input_login():

    #Captura as informações de login que serão recebidas do chat
    matricula = input('Digite a matrícula (somente os numeros):\n')
    senha = input('Digite a senha:\n')

    #Usando expressões regulares para ter certeza que o usuario inseriu
    #a matricula no formato correto
    r = re.compile('\d{10}')
    matricula = r.findall(matricula)
    #Repete a aquisição da matricula até que o usuario insira no formato correto
    while (len(matricula) < 1):
        matricula = input('A matrícula não está no formato correto (xxxxxxxxxx) :/\n'
                          'Digite ela novamente, por favor:\n')
        matricula = r.findall(matricula)

    #Pegando somente o primeiro match da lista gerada no regex
    matricula = matricula[0]

    #Chama a função de login do scraping para poder obter os dados do
    #usuario e os livros que podem ser renovados
    Scraping.login(matricula, senha)

    #Usa regex para pegar somente o primeiro nome do usuário
    r = re.compile('\w+')
    print("Olá, {0}".format(r.findall(Scraping.usuario)[0].capitalize()))

    #Livros para renovar, colocar os true or false no indice do livro a renovar
    livros_renovar=[True, True, False]

    scraping(livros_renovar)

#função separada só para poder chamar ou não
def scraping(livros_renovar):

    Scraping.renovacao(livros_renovar)

    if len(Scraping.livros)>0:
        print(Scraping.id_livros)
        print(Scraping.renov_livros)
        print(Scraping.renov_status)

#Função para não precisar dar inputs quando quiser testar funções
def login_automatico():
    # Carrega os json para credenciamento para
    # evitar que façamos o commit das nossas credenciais
    with open('credenciais.json') as data_file:
        data_params = json.load(data_file)

    # Livros para renovar, colocar os true or false no indice do livro a renovar
    livros_renovar = [True, True, False]
    Scraping.login(data_params['login']['codigo'], data_params['login']['senha'])
    Scraping.renovacao(livros_renovar)

    if len(Scraping.livros) > 0:
        print(Scraping.usuario)
        print(Scraping.livros)
        print(Scraping.id_livros)
        print(Scraping.renov_livros)
        print(Scraping.renov_status)

#Chama a função para realizar os inputs pelo usuario
input_login()

'''
#Opção de automatizar os inputs em testes
login_automatico()
'''