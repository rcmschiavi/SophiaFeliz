from operacoes.ChatBot import *
from .utils import post_facebook_message
from chatterbot import ChatBot

def operacao(id_face, mensagem):
    """ Função para realizar as operações de acordo com a necessidade, segue a lista das op e significados
    -1 - Não possui cadastro nenhum
    0 - Cadastrar Matrícula
    1 - Recebendo Matrícula
    2 - Não possui senha
    3 - Cadastrando senha
    4 - Possui cadastro completo, renovações em dia
    5 - Requisitando renovação
    6 - Recebendo dados renovação
    """
    post_facebook_message(id_face, "Vou procurar você aqui no meu banco de dados...")

    try:
        operacao = select_info_user_db(id_face)[0][4]
        post_facebook_message(id_face, "Te achei :)")
    except:
        post_facebook_message(id_face,"erro")
        operacao = -1

    if operacao==-1:
        post_ola(id_face)
        operacao=0
    elif operacao==0:
        post_matricula(id_face)
    elif operacao==1:
        get_matricula(id_face, mensagem)
    elif (operacao ==2):
        post_senha(id_face)
    elif operacao ==3:
        get_senha(id_face,mensagem)


def teste(verificar = False):
    return verificar

def respauto(id_face, mensagem):
    chatterbot = ChatBot("Sophia", trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
    chatterbot.train("chatterbot.corpus.portuguese")
    resposta = chatterbot.get_response(mensagem)
    post_facebook_message(id_face, str(resposta))