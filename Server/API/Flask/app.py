from flask import Flask, make_response, request, jsonify
from dataBase import Connection
from controle import verificaUser, verificaAccount
from dotenv import load_dotenv
from pathlib import Path
import os

try:
    dotenv_path = Path('./.env')
    load_dotenv(dotenv_path=dotenv_path)
except:
    pass

host_name = os.getenv('MYSQL_HOSNAME')
user_name = os.getenv('MYSQL_USER')
user_password = os.getenv('MYSQL_PASSWORD')
db_name = os.getenv('MYSQL_DATABASE')
c = Connection(host_name, user_name, user_password, db_name)

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    user = request.json
    """ 
    TODO
    QUESTÃO DA SEGURANÇA DA REQUISIÇÃO
    """ 
    if(c.create_user(nome=user["nome"], senha=user["senha"])):
        data = {
            'nome':user["nome"],
            'senha':'{0}'.format(user["senha"])
        }
        return make_response(
            jsonify(
                user=data
            )
        ) 
    return [None]

@app.route('/login', methods=['POST'])
def login():
    user = request.json
    """ 
    TODO
    QUESTÃO DA SEGURANÇA DA REQUISIÇÃO
    """ 
    
    r = c.search_user(where="nome = '{0}' and senha = '{1}'".format(user["nome"], user["senha"]))
    if(not r):
        return [None]
    if(len(r) == 1):
        data = {
            'nome':r[0][1],
            'senha':r[0][2]
        }
        return make_response(
            jsonify(
                user=data
            )
        )
    else:
        return [None]

@app.route('/set_account', methods=['POST'])
def set_account():
    try:
        idUser = verificaUser(request.json["user"], c)
        data = request.json["data"]
        if(idUser == 0):
            return ["no user find"]
        if(c.create_account(bank=data["banco"], typ=data["tipo"], date=data["data"], idUser=idUser, money=data["dinheiro"])):
            return data
        return ["error to find user"]
    except KeyError as e:
        if(str(e) == "'user'"):
            return ["missing user"]
        if(str(e) == "'data'"):
            return ["missing data"]
        else:
            return ["account data error"]

@app.route('/get_account', methods=['GET', 'POST'])
def get_account():
    try:
        # account = request.json
        # keys = list(account.keys())
        # values = list(account.values())
        # where = ""
        idUser = verificaUser(request.json["user"], c)
        if(idUser == 0):
            return ["no user find"]

        where = "id_usuario = {0} ".format(idUser)
        # for i in range(len(account)):
        #     print(keys[i], values[i])
        #     if(keys[i] != "user"):
        #         if(i!=0):
        #             where= where+"and "
        #         where = where+"{0} = '{1}' ".format(keys[i], values[i])
        return make_response(
            c.search_account(where=where)
        )
    except:
        return ["error"]

@app.route('/delete_account', methods=['DELETE'])
def delete_account():
    try:
        # account = request.json
        # keys = list(account.keys())
        # values = list(account.values())
        # where = ""
        idUser = verificaUser(request.json["user"], c)
        idAccount = request.json["data"]["id"]
        if(idUser == 0):
            return ["no user find"]

        if(verificaAccount(idUser, idAccount, c) == 0):
            return ["no account find"]

        deleted = c.search_account(where="id = {0}".format(idAccount))

        c.remove_account(where="id = {0}".format(idAccount))

        return make_response(
            deleted
        )
    except:
        return ["error"]

@app.route('/set_routines', methods=['POST'])
def set_routines():
    routines = request.json
    print(routines)
    c.create_routines(typ=routines["tipo"], typR=routines["tipo_r"], value=routines["valor"], iniDate=routines["dataB"], date=routines["data"], desc=routines["desc"], idConta=routines["id_conta"])
    return routines

@app.route('/get_routines', methods=['GET', 'POST'])
def get_routines():
    try:
        routines = request.json
        keys = list(routines.keys())
        values = list(routines.values())
        where = ""
        idUser = c.search_user(where="nome = '{0}' and senha = {1}".format(routines["user"]["nome"], routines["user"]["senha"]))[0][0]
        accounts = c.search_account(where="id_usuario = {0}".format(idUser))
        if(len(accounts) == 0):
            return [None]
        where = "id_conta in ("
        for a in range(len(accounts)):
            if(a!=0):
                where+=", "
            where = where+str(accounts[a][0])
        where = where+") "
        for i in range(len(routines)):
            print(keys[i], values[i])
            if(keys[i] != "user"):
                if(i!=0):
                    where= where+"and "
                where = where+"{0} = '{1}' ".format(keys[i], values[i])
        print(where)
        
        return make_response(
            c.search_routines(where=where)
        )
    except:
        print("fail")
        return make_response(
            c.search_routines()
        ) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')