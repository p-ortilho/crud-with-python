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
comand_sql = 'DELETE FROM produtos WHERE id=3'

#Executando comando SQL
cursor.execute(comand_sql)

#Toda modificação feita no banco é preciso commitar
mysqlConnection.commit()

#Fechando conexão e cursor
cursor.close()
mysqlConnection.close()