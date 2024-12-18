import mysql.connector
from mysql.connector import Error

class BaseModel(object):
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )

    # Função para criar um hash simples
    def simple_hash(self, input_string):
        hash_value = 0
        for char in input_string:
            # Realiza operações básicas usando o valor ASCII
            hash_value = (hash_value * 31 + ord(char)) % (10**8)  # Usa módulo para limitar o tamanho do hash
        return str(hash_value)

    def close(self):
        if self.connection.is_connected():
            # self.cursor.close()
            self.connection.close()
            print("Conexão ao MySQL encerrada.")