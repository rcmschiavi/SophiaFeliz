#!/usr/bin/python
# -*- coding: utf-8 -*-
import schedule
import Scraping
import Manager_DB
import ChatBot
import re
import datetime
import time
from datetime import datetime, date, timedelta
from sophia.chatbot.utils import post_facebook_message
from sophia import Comandos_shell

def automatico():
    data_limite = date.today()  + timedelta(days=6)
    #date_limite =
    print(data_limite)
    Manager_DB.connect_db()
    rows_renov = Manager_DB.select_livros()

    print(rows_renov)

    for row in rows_renov:
        if((row[1]!=None)and(int(row[2])==1)):
            data_venc = datetime.strptime(row[1], '%d/%m/%y')
            if(data_venc.date()<data_limite):
               print(row[1])
               print("Você tem um livro para renovar.")
               # Testando a desativação das notificações
               if (input('Você deseja desligar as notificações? (y/n) ') == 'y'):
                   Manager_DB.ignorar_avisos(row[0])
                   print("As notificações foram desativadas")
            else: print("Não há livros que vencerão em breve.")
        else: print("Não há livros ativos para renovar.")

    Manager_DB.select_livros()

def chat(id_face):
    """ Função para realizar as operações quando receber requesições do chatBot """

    livros_renovar = []

    # Abre o DB para realizar as operações
    Manager_DB.connect_db()

    # Define a variável com uma lista dos matchs de id_face com os registros do DB
    dados_db = Manager_DB.select_info_user(id_face)

    # Verifica se o id_facebook já está registrado, else faz o registro
    if (dados_db == []):
        print("Ainda não tenho sua matricula e senha.")
        matricula, senha = ChatBot.get_credenciais()
        Manager_DB.insert_cred(id_face,matricula,senha)
        dados_db = Manager_DB.select_info_user(id_face)
    else:
        matricula, senha = dados_db[0][2], dados_db[0][3]
        print("Já tenho suas credenciais.")
    print("Matrícula: {0} Senha1: {1}".format(matricula,senha))

    # Exit para realizar os testes sem fazer nenhum scraping
    #exit(0)

    print('Tentando login...')

    # Chama a função de login do scraping para poder obter os dados do
    #usuario e os livros que podem ser renovados
    Scraping.login(matricula, senha)

    # Realiza o select no DB para verificar se já temos
    # as credenciais do usuario pelo id_face
    Manager_DB.select(id_face)

    # Usa regex para pegar somente o primeiro nome do usuário
    r = re.compile('\w+')
    print("Olá, {0}".format(r.findall(Scraping.usuario)[0].capitalize()))

    # Prossegue as operações caso haja algum livro na biblioteca
    if(len(Scraping.livros)>0):

        # Exibe os livros com as datas de vencimento
        print("Você tem os seguintes livros com as respectivas datas de vencimento:")
        for i in Scraping.livros:
            print("id: {0}  livro: {1}  vencimento: {2}".format(Scraping.livros.index(i)+1,i,Scraping.prazos[Scraping.livros.index(i)]))

        # verifica qual das datas de vencimento
        venc_prox = Scraping.prazos[0]
        for i in Scraping.prazos:
            if(i<venc_prox):
                venc_prox=i
        Manager_DB.update_vencimento(dados_db[0][0],venc_prox)

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
            # Mesma indexação utilizada na verificação do input de renovação
            print("livro: {0} resultado: {1}".format(i,Scraping.renov_status[Scraping.renov_livros.index(i)]))

    else: print("Você não possui livros para renovar")

    # Fecha o DB
    Manager_DB.conn.close()

# Chama a função para realizar as operações pelo chat
#chat()
print("     Inciando atividades...")
# Realiza a atividade todos os dias no mesmo horário, verificar horário do server
###schedule.every().day.at("03:00").do(automatico)

# Para testes é mais interessante realizar operação a cada minuto
schedule.every().minute.do(automatico)
Comandos_shell.tunnel()
print("     Portas abertas...")

while True:
    schedule.run_pending()
    time.sleep(5) # wait one minute