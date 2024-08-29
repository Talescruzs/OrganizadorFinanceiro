import mysql.connector
from datetime import date, time, datetime
from mysql.connector import Error


class Connection(object):
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
        # self.cursor = self.connection.cursor()

    def create_database(self):
        cursor = self.connection.cursor()
        try:
            # Conectar ao servidor MySQL
            if self.connection.is_connected():
                # Criar banco de dados
                cursor.execute(f'''CREATE DATABASE IF NOT EXISTS {self.db_name}''')
                print(f"Banco de dados '{self.db_name}' criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            cursor.close()

    def create_tables(self):
        cursor = self.connection.cursor()
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Criar uma tabela
                create_table_query = f'''
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    senha VARCHAR(45) NOT NULL,
                )'''
                cursor.execute(create_table_query)
                print(f"Tabela Usuarios criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f'''
                CREATE TABLE IF NOT EXISTS Contas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    banco VARCHAR(100) NOT NULL,
                    tipo VARCHAR(1),
                    saldo float NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    id_usuario INT,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
                )'''
                cursor.execute(create_table_query)
                print(f"Tabela Contas criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f'''
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
                )'''
                cursor.execute(create_table_query)
                print(f"Tabela Rotinas criada com sucesso no banco de dados '{self.db_name}'!")
                create_table_query = f'''
                CREATE TABLE IF NOT EXISTS Historico (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    tipo VARCHAR(1) NOT NULL,
                    valor FLOAT,
                    descricao VARCHAR(300),
                    id_conta INT,
                    FOREIGN KEY (id_conta) REFERENCES Contas(id) ON DELETE CASCADE
                )'''
                cursor.execute(create_table_query)
                print(f"Tabela Historico criada com sucesso no banco de dados '{self.db_name}'!")
        except Error as e:
            print(f"Erro ao criar a tabela: {e}")
        finally:
            cursor.close()

    def __insert(self, table: str, columns: str, values: str):
        cursor = self.connection.cursor()
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                insert_user_query = '''
                INSERT INTO {0} ({1})
                VALUES ({2});
                '''.format(table, columns, values)
                cursor.execute(insert_user_query)
                self.connection.commit()  # Confirmar a transação
            print(f"'{values}' inserido com sucesso na tabela '{table}'!")
            return True
        except Error as e:
            print(f"Erro ao inserir {table}: {e}")
            return False
        finally:
            cursor.close()

    def __select(self, table: str, columns: str, where: str):
        cursor = self.connection.cursor()
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT {columns} FROM {table} WHERE {where}"
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                return results
            print(f"{table} '{results}'")
        except Error as e:
            print(f"Erro no select {table}: {e}")
            return False
        finally:
            cursor.close()

    def __delete(self, table: str, where: str):
        cursor = self.connection.cursor()
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"DELETE FROM {table} WHERE {where}"
                self.cursor.execute(query)
                self.connection.commit()
            print(f"{table}(s) removido(s) onde {where}.")
            return True
        except Error as e:
            print(f"Erro ao remover {table}: {e}")
            return False
        finally:
            cursor.close()

    def create_user(self, nome: str, senha: str):
        return self.__insert(table="Usuarios", columns="nome, senha", values="'{0}', '{1}'".format(nome, senha))

    def search_user(self, columns: str = "*", where: str = "1=1"):
        return self.__select(table="Usuarios", columns=columns, where=where)

    def remove_user(self, where: str = "1=1"):
        return self.__delete(table="Usuarios", where=where)

    def create_account(self, bank: str, typ: str, date: datetime, idUser: int, money: float = 0.0):
        return self.__insert(
            table="Contas",
            columns="banco, tipo, saldo, data_criacao, id_usuario",
            values="'{0}', '{1}', {2}, '{3}', {4}".format(bank, typ, money, date, idUser)
        )

    def search_account(self, columns: str = "*", where: str = "1=1"):
        return self.__select(table="Contas", columns=columns, where=where)

    def remove_account(self, where: str = "1=1"):
        return self.__delete(table="Contas", where=where)

    def create_routines(self, typ: str, typR: str, value: float, iniDate: datetime, date: datetime, desc: str, idConta: int):
        return self.__insert(
            table="Rotinas",
            columns="tipo, tipo_repeticao, valor, data_base, data_criacao, foi_add_manual, descricao, id_conta",
            values="'{0}', '{1}', {2}, '{3}', '{4}', {5}, '{6}', {7}".format(typ, typR, value, iniDate, date, 0, desc,
                                                                             idConta
                                                                             )
        )

    def search_routines(self, columns: str = "*", where: str = "1=1"):
        return self.__select(table="Rotinas", columns=columns, where=where)

    def remove_routines(self, where: str = "1=1"):
        return self.__delete(table="Rotinas", where=where)

    def create_historic(self, date: datetime, typ: str, value: float, desc: str, idConta: int):
        return self.__insert(
            table="Historico",
            columns="data_criacao, tipo, valor, descricao, id_conta",
            values="'{0}', '{1}', {2}, '{3}', {4}".format(date, typ, value, desc, idConta)
        )

    def search_historic(self, columns: str = "*", where: str = "1=1"):
        return self.__select(table="Historico", columns=columns, where=where)

    def remove_historic(self, where: str = "1=1"):
        return self.__delete(table="Historico", where=where)

    def close_connection(self):
        if self.connection.is_connected():
            # self.cursor.close()
            self.connection.close()
            print("Conexão ao MySQL encerrada.")


if __name__ == "__main__":
    # Parâmetros de conexão
    host_name = "localhost"
    user_name = "root"
    user_password = "senha"
    db_name = "Financas"

    # Chamar a função para criar o banco de dados
    connect = Connection(host_name, user_name, user_password, db_name)
    # connect.create_database()
    # connect.create_tables()
    r = connect.create_user(nome="Tales", senha="123")
    r = connect.search_user(where="nome = 'Tales'")
    idUser = r[0][0]

    for a in r:
        print("id: {0} nome: {1}".format(a[0], a[1]))

    r = connect.create_account(bank="Banrisul", typ="P", date=datetime.today(), idUser=idUser, money=1000.50)
    r = connect.search_account()
    for a in r:
        print("id: {0} nome: {1}".format(a[0], a[1]))
    idConta = r[0][0]
    r = connect.create_routines(
        typ="I",
        typR="M",
        value=1120,
        iniDate=datetime(2024, 8, 14),
        date=datetime.today(),
        desc="Salario de estágio TCU",
        idConta=idConta
    )
    r = connect.search_routines()
    for a in r:
        print("id: {0} Tipo: {1} Valor {2}".format(a[0], a[1], a[3]))

    r = connect.create_historic(
        date=datetime(2024, 8, 14),
        typ="I",
        value=1120,
        desc="Salario de estágio TCU",
        idConta=idConta
    )
    r = connect.search_historic()
    for a in r:
        print("id: {0} Tipo: {1} Valor {2}".format(a[0], a[2], a[3]))


    connect.remove_historic("id_conta = {0}".format(idConta))
    connect.remove_routines("id_conta = {0}".format(idConta))
    connect.remove_account("id_usuario = {0}".format(idUser))
    connect.remove_user("nome = 'Tales'")
    connect.close_connection()
