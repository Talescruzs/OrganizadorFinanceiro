from dataBase import Connection

def verificaUser(user:dict, c:Connection) -> int:
    u = c.search_user(where="nome = '{0}' and senha = {1}".format(user["nome"], user["senha"]))
    if(not u):
        return 0
    if(len(u)==1):
        return u[0][0]
    return 0