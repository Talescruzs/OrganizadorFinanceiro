import mysql.connector
from mysql.connector import Error
from datetime import date, time, datetime
from models.baseModel import BaseModel

class MovementModel(BaseModel):
    def __init__(self, host_name, user_name, user_password, db_name):
        super().__init__(host_name, user_name, user_password, db_name)

    def insetMovement(self, desc, idAccountIni, idAccountEnd, idUser, value, date):
        cursor = self.connection.cursor()
        # try:
        if self.connection.is_connected():
            insert_user_query = '''
            INSERT INTO movimentacoes (`desc`, conta_ini, conta_fim, fk_usuario, valor, data)
            VALUES (%s, %s, %s, %s, %s, %s);
            '''
            values = (desc, idAccountIni, idAccountEnd, idUser, value, date)
            cursor.execute(insert_user_query, values)
            self.connection.commit()
            cursor.close()
            return True
        # except Error as e:
        #     cursor.close()
        #     return False
    def selectMovementsByAccount(self, idAccount):
        cursor = self.connection.cursor()
        response = 0
        try:
            if self.connection.is_connected():
                query = f"SELECT * FROM movimentacoes WHERE conta_ini = {idAccount} or conta_fim = {idAccount}"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                response = results
            return response
        except Error as e:
            cursor.close()
            return response
    
    def deleteMovementById(self, idMovement):
        response = False
        cursor = self.connection.cursor()
        try:
            if self.connection.is_connected():
                query = "DELETE FROM movimentacoes WHERE id = %s"
                cursor.execute(query, (idMovement,))
                self.connection.commit()
                response = True
        except Exception as e:
            print(f"Erro ao excluir a conta com ID {idMovement}: {e}")
        finally:
            cursor.close()
            return response