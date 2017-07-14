# -*- coding: utf-8 -*-

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
    VALUES  ((SELECT id  FROM usuarios WHERE id_face LIKE '%s'))
    """% (id_face))
    conn.commit()

