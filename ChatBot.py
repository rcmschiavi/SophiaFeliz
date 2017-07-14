import getpass
import re

def get_face():
    ''' Função para simular o id_face recebido no post do ChatBot '''

    id_face = input('Digite o id')
    return id_face

def get_credenciais():
    ''' Função para simular a aquisição das credenciais pelo Chat '''

    # Captura as informações de login que serão recebidas do chat
    matricula = input('Digite a matrícula (somente os numeros):\n')

    # Usando expressões regulares para ter certeza que o usuário inseriu
    #a matricula no formato correto
    r = re.compile('\d{10}')
    matricula = r.findall(matricula)
    # Repete a aquisição da matricula até que o usuario insira no formato correto
    while (len(matricula) < 1):
        matricula = input('A matrícula não está no formato correto (xxxxxxxxxx) :/\n'
                          'Digite ela novamente, por favor:\n')
        matricula = r.findall(matricula)

    # Pede senha após a matrícula estar correta.
    senha = input('Digite a senha:')

    # Define como matricula somente o primeiro match da lista gerada no regex
    matricula = matricula[0]

    return  matricula, senha