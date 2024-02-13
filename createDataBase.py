#Importando biblioteca
import mysql.connector

#Criando a conexão com banco de dados
mysqlConnection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='root',
)

#Criando a interação com o banco de dados
cursor = mysqlConnection.cursor()

#Criando a DATA BASE
cursor.execute('CREATE DATABASE mercearia')

#Fechando conexão e cursor
cursor.close()
mysqlConnection.close()