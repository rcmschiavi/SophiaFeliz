# -*- coding: utf-8 -*-

# Realiza os procedimentos de gerenciamento do banco de dados
# Faz as inserções das credenciais dos usuários
# Também registra a data de vencimento mais próxima para evitar a operação de login no processo automático
# Que avisará o usuário que o livro está perto de vencer

import sqlite3

cursor, conn = sqlite3.Cursor, sqlite3.Connection

def abrir_db():
    """ Função que abre o DB """

    global cursor, conn
    try:
        conn = sqlite3.connect('SophiaDB.db')
        cursor = conn.cursor()
    except Exception as e:
        print("Erro ao abrir o banco de dados: ", e)
        exit(-1)

def select(id_face):
    """ Função para verificar se o id_face já está presente no DB """

    global cursor,conn
    cursor.execute("""
    SELECT * FROM usuarios
    WHERE id_face LIKE '%s'
    """% (id_face))
    return cursor.fetchall()

def insert_cred(id_face, matricula, senha):
    """ Função para inserir as credenciais no DB """

    global cursor
    cursor.execute("""
    INSERT INTO usuarios (id_face, matricula, senha)
    VALUES (?,?,?)
    """, (id_face, matricula, senha))

    cursor.execute("""
    INSERT INTO renovacoes (id)
    VALUES  ((SELECT id  FROM usuarios WHERE id_face LIKE '%d'))
    """% (int(id_face)))
    conn.commit()

def update_vencimento(id,vencimento):
    """ Função para atualizar a data de renovação mais próxima """

    global cursor
    cursor.execute("""
       UPDATE renovacoes
    SET vencimento = '%s'
    WHERE id = '%d';
    """% (vencimento,int(id)))
    print(int(id),vencimento)
    conn.commit()

def verificar_datas(id):
    """ Função para verificar a data de vencimento registrada no DB sem fazer o scraping """

    global cursor
    cursor.execute("""
    SELECT vencimento FROM renovacoes
    WHERE id LIKE '%s'
    """% (int(id)))

def update_senha(id_face, nova_senha):
    " Função que realiza a troca de senha no DB"
    
    global cursor
    cursor.execute("""
       UPDATE usuario
    SET senha = '%s'
    WHERE id_face = '%d';
    """% (nova_senha,int(id_face)))
    conn.commit()
