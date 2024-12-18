from controllers.baseController import BaseController
from controllers.userController import UserController
from datetime import date, time, datetime

from models.accountModel import AccountModel


class AccountController(BaseController):
    def __init__(self):
        super().__init__()
    
    def createAccount(self, user, data):
        userId = UserController().userId(user['nome'], user['senha'], user['hash'])
        if userId == 0:
            return False

        model = AccountModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = False

        response = model.insertAccount(data['nomeBanco'], data['tipoConta'], data['valor'])
        if not response:
            model.close()
            return False
        
        accountId = model.accountId(data['nomeBanco'], data['tipoConta'], data['valor'])
        if accountId == 0: 
            model.close()
            return False

        date = datetime.now()
        valid = True

        if 'data' in data:
            date = data['data']
        if 'validade' in data:
            valid = data['validade']

        response = model.linkUserAccount(userId, accountId, date.date(), valid)
        model.close()
        return response

    def selectAccountById(self, accountId):
        model = AccountModel(self.host_name, self.user_name, self.user_password, self.db_name)
        accountById = model.selectAccountById(accountId)
        model.close()
        response = {
            'id':accountById[0],
            'nomeBanco':accountById[1],
            'tipo':accountById[2],
            'valor':accountById[3],
        }
        return response
    
    def deleteAccountById(self, user, accountId):
        userId = UserController().userId(user['nome'], user['senha'], user['hash'])
        if userId == 0:
            return False

        model = AccountModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = model.deleteAccountById(accountId)
        model.close()
        return response