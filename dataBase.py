import mysql.connector
from mysql.connector import Error

class Conection:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        self.connection = mysql.connector.connect(
            host=self.host_name,
            user=self.user_name,
            password=self.user_password,
            database=self.db_name
        )
        self.cursor = self.connection.cursor()

    def create_database(self):
        try:
            # Conectar ao servidor MySQL
            if self.connection.is_connected():
                # Criar banco de dados
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
                print(f"Banco de dados '{self.db_name}' criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar o banco de dados: {e}")
            
    def create_tables(self):
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Criar uma tabela
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL
                )"""
                self.cursor.execute(create_table_query)
                print(f"Tabela Usuarios criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS Contas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    banco VARCHAR(100) NOT NULL,
                    tipo VARCHAR(1),
                    saldo float NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    id_usuario INT,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
                )"""
                self.cursor.execute(create_table_query)
                print(f"Tabela Contas criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS Rotinas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    tipo VARCHAR(1) NOT NULL,
                    tipo_repeticao VARCHAR(1) NOT NULL,
                    valor FLOAT NOT NULL,
                    data_base TIMESTAMP NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    foi_add_manual INT NOT NULL,
                    descricao VARCHAR(300),
                    id_conta INT,
                    FOREIGN KEY (id_conta) REFERENCES Contas(id) ON DELETE CASCADE
                )"""
                self.cursor.execute(create_table_query)
                print(f"Tabela Rotinas criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS Historico (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    tipo VARCHAR(1) NOT NULL,
                    valor FLOAT,
                    descricao VARCHAR(300),
                    id_conta INT,
                    FOREIGN KEY (id_conta) REFERENCES Contas(id) ON DELETE CASCADE
                )"""
                self.cursor.execute(create_table_query)
                print(f"Tabela Historico criada com sucesso no banco de dados '{self.db_name}'!")     
        except Error as e:
            print(f"Erro ao criar a tabela: {e}")
            
    def create_user(self, nome:str):
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                insert_user_query = """
                INSERT INTO Usuarios (nome)
                VALUES (%s)
                """
                self.cursor.execute(insert_user_query, (nome,))
                self.connection.commit()  # Confirmar a transação
            print(f"Usuário '{nome}' inserido com sucesso na tabela 'Usuarios'!")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
            
    def search_user(self, columns:str = "*", where:str = "1=1"):
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT {columns} FROM Usuarios WHERE {where}"
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                return results
            print(f"Usuário '{results}'")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")

    def remove_user(self, where:str = "1=1"):
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"DELETE FROM Usuarios WHERE {where}"
                self.cursor.execute(query)
                self.connection.commit()
            print(f"Usuário(s) removido(s) onde {where}.")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão ao MySQL encerrada.")

if __name__ == "__main__":
    # Parâmetros de conexão
    host_name = "localhost"
    user_name = "root"
    user_password = "*"
    db_name = "Financas"

    # Chamar a função para criar o banco de dados
    connect = Conection(host_name, user_name, user_password, db_name)
    # connect.create_database()
    # connect.create_tables()
    # r =connect.create_user(nome="Teste")
    # r = connect.search_user(where="nome = 'Teste'")
    # for a in r:
    #     print("id: {0} nome: {1}".format(a[0], a[1]))
    # connect.remove_user("nome = 'Tales'")

    connect.close_connection()
