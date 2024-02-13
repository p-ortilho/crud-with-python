#Importando biblioteca
import mysql.connector

#Criando a conexão com banco de dados
mysqlConnection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='root',
    database='mercearia'
)

#Criando a interação com o banco de dados
cursor = mysqlConnection.cursor()

#Comando SQL 
comand_sql = 'SELECT * FROM produtos'

#Comando SQL 
#comand_sql = 'SELECT nome FROM produtos'

#Executando nosso comando SQL
cursor.execute(comand_sql)

#Pegando os dados da consulta feita na tabela
consulta = cursor.fetchall()

#Imprimindo cada valor retornado na consulta
for i in consulta:
    print(i)

#Fechando conexão e cursor
cursor.close()
mysqlConnection.close()