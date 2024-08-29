from dataBase import Connection

def verificaUser(user:dict, c:Connection) -> int:
    u = c.search_user(where="nome = '{0}' and senha = {1}".format(user["nome"], user["senha"]))
    if(not u):
        return 0
    if(len(u)==1):
        return u[0][0]
    return 0

def verificaAccount(userID:int, accountID:int, c:Connection) -> int:
    u = c.search_account(where="id_usuario = {0} and id = {1}".format(userID, accountID))
    if(not u):
        return 0
    if(len(u)==1):
        return u[0][0]
    return 0