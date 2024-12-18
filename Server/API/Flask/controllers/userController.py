from controllers.baseController import BaseController
from models.userModel import UserModel


class UserController(BaseController):
    def __init__(self):
        super().__init__()
    
    def register(self, name, password, email):
        model = UserModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = model.register(name, password, email)
        model.close() 
        return response

    def login(self, name, password, hashCode):
        model = UserModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = model.login(name, password, hashCode)
        model.close() 
        return response

    def user(self, name, password, hashCode):
        model = UserModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = model.user(name, password, hashCode)
        model.close() 
        return response
    
    def userId(self, name, password, hashCode):
        model = UserModel(self.host_name, self.user_name, self.user_password, self.db_name)
        response = model.userId(name, password, hashCode)
        model.close() 
        return response
