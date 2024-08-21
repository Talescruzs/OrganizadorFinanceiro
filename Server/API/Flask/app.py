from flask import Flask, make_response, request, jsonify
from dataBase import Connection
import sys

# Para rodar: /caminho/app.py localhost root senha dataBase

host_name = sys.argv[1]
user_name = sys.argv[2]
user_password = sys.argv[3]
db_name = sys.argv[4]
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
    return [None]

@app.route('/set_account', methods=['POST'])
def set_account():
    account = request.json
    print(account)
    print(account["user"])
    idUser = c.search_user(where="nome = '{0}' and senha = {1}".format(account["user"]["nome"], account["user"]["senha"]))[0][0]
    c.create_account(bank=account["banco"], typ=account["tipo"], date=account["data"], idUser=idUser, money=account["dinheiro"])
    return account

@app.route('/get_account', methods=['GET', 'POST'])
def get_account():
    try:
        account = request.json
        keys = list(account.keys())
        values = list(account.values())
        where = ""
        idUser = c.search_user(where="nome = '{0}' and senha = {1}".format(account["user"]["nome"], account["user"]["senha"]))[0][0]
        print(idUser)
        where = "id_usuario = {0} ".format(idUser)
        for i in range(len(account)):
            print(keys[i], values[i])
            if(keys[i] != "user"):
                if(i!=0):
                    where= where+"and "
                where = where+"{0} = '{1}' ".format(keys[i], values[i])
        return make_response(
            c.search_account(where=where)
        )
    except:
        return [None]

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