from controllers.baseController import BaseController
from controllers.userController import UserController
from datetime import date, time, datetime

from models.movementModel import MovementModel


class MovementController(BaseController):
    def __init__(self):
        super().__init__()
    
    def createMovement(self, user, data):
        userId = UserController().userId(user['nome'], user['hash'])
        if userId == 0:
            return False

        model = MovementModel(self.host_name, self.user_name, self.user_password, self.db_name)

        idAccountIni = None
        idAccountEnd = None
        date = datetime.now()
        if 'conta_ini' in data:
            idAccountIni = data['conta_ini']
        if 'conta_fim' in data:
            idAccountEnd = data['conta_fim']
        if 'data' in data:
            date = data['data']

        response = model.insetMovement(data['desc'], idAccountIni, idAccountEnd, userId, data['valor'], date)
        
        model.close()
        return response

    def selectMovementsByAccount(self, accountId):
        model = MovementModel(self.host_name, self.user_name, self.user_password, self.db_name)
        movements = model.selectMovementsByAccount(accountId)
        model.close()
        response = list()
        for m in movements:
            response.append(
                {
                    'desc': m[1],
                    'conta_ini': m[2],
                    'conta_fim': m[3],
                    'fk_usuario': m[4],
                    'valor': m[5],
                    'data': m[6]
                }
            )
        return response
    
    # def deleteAccountById(self, user, accountId):
    #     userId = UserController().userId(user['nome'], user['hash'])
    #     if userId == 0:
    #         return False

    #     model = AccountModel(self.host_name, self.user_name, self.user_password, self.db_name)
    #     response = model.deleteAccountById(accountId)
    #     model.close()
    #     return response