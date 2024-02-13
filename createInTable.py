#Importando biblioteca
import mysql.connector

#Variaveis com valores para serem inseridos no DB
produto = 'leite'
produto_valor = 4.59

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

#Criando comando SQL 
comand_sql = f'INSERT INTO produtos (nome, valor) VALUES ("{produto}", {produto_valor})'

#Executando nosso comando SQL
cursor.execute(comand_sql)

#Toda modificação feita no banco é preciso commitar
mysqlConnection.commit()

#Fechando conexão e cursor
cursor.close()
mysqlConnection.close()