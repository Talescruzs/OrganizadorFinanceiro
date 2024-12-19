import mysql.connector
from mysql.connector import Error
from datetime import date, time, datetime
from models.baseModel import BaseModel

class UserModel(BaseModel):
    def __init__(self, host_name, user_name, user_password, db_name):
        super().__init__(host_name, user_name, user_password, db_name)

    def register(self, name, password, email):
        data = name + password + email
        hashCode = self.simple_hash(data)

        cursor = self.connection.cursor()
        try:
            if self.connection.is_connected():
                insert_user_query = '''
                INSERT INTO usuarios (senha, autenticador, nome, email)
                VALUES (%s, %s, %s, %s);
                '''
                values = (password, hashCode, name, email)
                cursor.execute(insert_user_query, values)
                self.connection.commit()  # Confirmar a transação
                print(f"Inserido com sucesso na tabela!")
                cursor.close()
            return hashCode
        except Error as e:
            print(f"Erro ao inserir: {e}")
            cursor.close()
            return '0'

    def login(self, name, password):
        cursor = self.connection.cursor()
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT * FROM usuarios WHERE nome = '{name}' and senha = '{password}'"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                if len(results) == 1:
                    return results[0][2]
            return False
        except Error as e:
            print(f"Erro no select: {e}")
            cursor.close()
            return False

    def user(self, name, password, hashCode):
        cursor = self.connection.cursor()
        response = {
            'name': '',
            'email': '',
            'hashCode': ''
        }
        try:
            # Conectar ao banco de dados MySQL
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT * FROM usuarios WHERE nome = '{name}' and senha = '{password}' and autenticador = '{hashCode}'"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                if len(results) == 1:
                    response['hashCode'] = results[0][2]
                    response['name'] = results[0][3]
                    response['email'] = results[0][4]
            return response
        except Error as e:
            print(f"Erro no select: {e}")
            cursor.close()
            return response

    def userId(self, name, password, hashCode):
        cursor = self.connection.cursor()
        response = 0
        try:
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT * FROM usuarios WHERE nome = '{name}' and autenticador = '{hashCode}'"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                if len(results) == 1:
                    response = results[0][0]
            return response
        except Error as e:
            print(f"Erro no select: {e}")
            cursor.close()
            return response

    def selectUserAccounts(self, name, hashCode):
        userId = self.userId(name, hashCode)
        if(userId == 0):
            return 0

        cursor = self.connection.cursor()
        try:
            if self.connection.is_connected():
                # Inserir um novo usuário
                query = f"SELECT * FROM usuario_conta WHERE fk_usuario = {userId}"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()

                response = results
            return response
        except Error as e:
            print(f"Erro no select: {e}")
            cursor.close()
            return response