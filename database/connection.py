import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SILas?13",
        database="natacao_app"
    )

    return conexao