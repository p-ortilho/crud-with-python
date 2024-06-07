# crud-with-python

> Este repositório foi criado com o objetivo específico de aprimorar as habilidades em operações CRUD (Criar, Ler, Atualizar e Deletar). Utilizamos a linguagem de programação Python, conhecida por sua legibilidade e eficiência, em conjunto com o MySQL. Ao trabalhar com essas tecnologias, estamos desenvolvendo competências essenciais relacionadas à manipulação e gestão de bancos de dados. Isso inclui a criação de tabelas e registros (Criar), a recuperação de dados (Ler), atualização de registros existentes (Atualizar) e a remoção de registros ou tabelas (Deletar).

# Informações
Para o desenvolvimento deste repositório, empregamos um container MySQL, que atuou como nosso banco de dados. Isso facilitou significativamente o processo de desenvolvimento, permitindo uma implementação mais eficiente e eficaz. Para criar o container, foi utilizado o seguinte comando:
~~~
docker run --name crud_mysql_py -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql 
~~~

Para a utilização do script Python, é necessário fazer o download da biblioteca mysql.connector. Segue o comando para tal utilização:
~~~
pip install mysql-connector-python
~~~
