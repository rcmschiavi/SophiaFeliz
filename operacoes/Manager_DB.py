# -*- coding: utf-8 -*-

# Realiza os procedimentos de gerenciamento do banco de dados
# Faz as inserções das credenciais dos usuários
# Também registra a data de vencimento mais próxima para evitar a operação de login no processo automático
# Que avisará o usuário que o livro está perto de vencer

import sqlite3
import os

cursor, conn = sqlite3.Cursor, sqlite3.Connection

def connect_db():
    """ Função que abre o DB """

    global cursor, conn
    try:
        conn = sqlite3.connect(os.path.realpath('SophiaDB.db'))
        cursor = conn.cursor()
    except Exception as e:
        print("Erro ao abrir o banco de dados: ", e)
        exit(-1)

def select_info_user_db(id_face):
    """ Função para verificar se o id_face já está presente no DB """

    global cursor,conn
    cursor.execute("""
    SELECT * FROM usuarios
    WHERE id_face LIKE '%s'
    """% (id_face))
    return cursor.fetchall()

def insert_id_face_db(id_face, operacao):
    """ Função para inserir as credenciais no DB """

    global cursor, conn
    cursor.execute("""
    INSERT INTO usuarios (id_face, operacao)
    VALUES (?,?)
    """, (id_face, operacao))
    conn.commit()
    connect_db()
    cursor.execute("""
    INSERT INTO renovacoes (id)
    VALUES  ((SELECT id  FROM usuarios WHERE id_face LIKE '%d'), 0)
    """% (id_face))
    conn.commit()

def update_matricula(id_face, matricula):
    global cursor
    cursor.execute("""
        UPDATE usuarios
     SET matricula = '%s', operacao = 2
     WHERE id_face = '%d';
     """ % (matricula, id_face))
    conn.commit()


def update_operacao(id_face, operacao):
    global cursor
    cursor.execute("""
       UPDATE usuarios
    SET operacao = '%s'
    WHERE id_face = '%d';
    """% (operacao,id_face))
    conn.commit()

def update_vencimento_db(id,vencimento):
    """ Função para atualizar a data de renovação mais próxima """

    global cursor
    cursor.execute("""
       UPDATE renovacoes
    SET vencimento = '%s', ignorar = 1
    WHERE id = '%d';
    """% (vencimento,int(id)))
    print(int(id),vencimento)
    conn.commit()

def verificar_datas_db(id):
    """ Função para verificar a data de vencimento registrada no DB sem fazer o scraping """

    global cursor
    cursor.execute("""
    SELECT vencimento FROM renovacoes
    WHERE id LIKE '%s'
    """% (int(id)))

def update_senha_db(id_face, senha):
    " Função que realiza a troca de senha no DB"

    global cursor
    cursor.execute("""
       UPDATE usuario
    SET senha = '%s',
    operacao = '%d
    WHERE id_face = '%d';
    """% (senha,4,id_face))
    conn.commit()

def select_livros_db():

    global cursor,conn
    cursor.execute("""
    SELECT * FROM renovacoes
    """)
    return cursor.fetchall()

def ignorar_avisos(id):

    global cursor
    cursor.execute("""
       UPDATE renovacoes
    SET ignorar = 0
    WHERE id = %d;
    """% (id))
    conn.commit()