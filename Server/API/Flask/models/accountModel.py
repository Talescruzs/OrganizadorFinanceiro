import mysql.connector
from mysql.connector import Error
from datetime import date, time, datetime
from models.baseModel import BaseModel

class AccountModel(BaseModel):
    def __init__(self, host_name, user_name, user_password, db_name):
        super().__init__(host_name, user_name, user_password, db_name)

    def insertAccount(self, bankName, accountType, value):
        cursor = self.connection.cursor()
        # try:
        if self.connection.is_connected():
            insert_user_query = '''
            INSERT INTO contas (nome_banco, tipo, valor)
            VALUES (%s, %s, %s);
            '''
            values = (bankName, accountType, value)
            cursor.execute(insert_user_query, values)
            self.connection.commit()
            cursor.close()
            return True
        # except Error as e:
        #     cursor.close()
        #     return False
        # finally:
        #     cursor.close()
        #     return False

    def accountId(self, bankName, accountType, value):
        cursor = self.connection.cursor()
        response = 0
        # try:
        if self.connection.is_connected():
            # Inserir um novo usuário
            query = f"SELECT * FROM contas WHERE nome_banco = '{bankName}' and tipo = '{accountType}' and valor = {value}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            if len(results) == 1:
                response = results[0][0]
        return response
        # except Error as e:
        #     cursor.close()
        #     return response


    def linkUserAccount(self, idUser, idAccount, date, valid):
        cursor = self.connection.cursor()
        # try:
        if self.connection.is_connected():
            insert_user_query = '''
            INSERT INTO usuario_conta (fk_usuario, fk_conta, data_vinculo, valida)
            VALUES (%s, %s, %s, %s);
            '''
            values = (idUser, idAccount, date, valid)
            cursor.execute(insert_user_query, values)
            self.connection.commit()
            cursor.close()
            return True
        # except Error as e:
        #     cursor.close()
        #     return False
        # finally:
        #     cursor.close()
        #     return False

    def selectAccountById(self, accountId):
        response = 0
        cursor = self.connection.cursor()
        if self.connection.is_connected():
            query = f"SELECT * FROM contas WHERE id = {accountId}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            if len(results) == 1:
                response = results
        return response[0]