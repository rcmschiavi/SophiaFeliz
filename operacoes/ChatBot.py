
# Realiza os procedimentos do chatbot
# Como envio de mensagens, captura das credenciais e pedidos de renovação

import re
from operacoes.Manager_DB import *
from chatbot.utils import post_facebook_message

def post_ola(id_face):
    connect_db()
    post_facebook_message(id_face, "Oláá")
    post_facebook_message(id_face, "Ainda não tenho sua matrícula e senha")
    insert_id_face_db(int(id_face),0)


def post_matricula(id_face):
    post_facebook_message(id_face, "Digite sua matrìcula, por favor")
    update_operacao(id_face,1)

def get_matricula(id_face, mensagem):

    # Usando expressões regulares para ter certeza que o usuário inseriu
    # a matricula no formato correto
    r = re.compile('\d{10}')
    matricula = r.findall(mensagem)
    # Repete a aquisição da matricula até que o usuario insira no formato correto
    while (len(matricula) < 1):
        post_facebook_message("Parece que a matrícula não está no formato correto")
        post_facebook_message(id_face, "Digite sua matrìcula de novo, por favor")
        return

    # Define como matricula somente o primeiro match da lista gerada no regex
    matricula = matricula[0]
    update_matricula(id_face,matricula)
    post_facebook_message(id_face, "Deu tudo certo.")

def post_senha(id_face):
    post_facebook_message(id_face, "Digite a sua senha da biblioteca, por favor.")

def get_senha(id_face, mensagem):
    ''' Função para simular a aquisição das credenciais pelo Chat '''

    update_senha_db(id_face, mensagem)
    post_facebook_message(id_face, "A senha foi cadastrada.")