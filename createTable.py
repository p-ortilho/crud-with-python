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

#Criando TABLE
cursor.execute(
    'CREATE TABLE produtos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, valor FLOAT NOT NULL)'
)

#Toda modificação feita no banco é preciso commitar
mysqlConnection.commit()

#Fechando conexão e cursor
cursor.close()
mysqlConnection.close()