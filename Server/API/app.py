from flask import Flask, make_response, request
from dataBase import Connection

host_name = "localhost"
user_name = "root"
user_password = "*"
db_name = "Financas"
c = Connection(host_name, user_name, user_password, db_name)
# c.create_user(nome="Teste", senha="123")

app = Flask(__name__)

@app.route('/set_user', methods=['POST'])
def set_user():
    user = request.json
    c.create_user(nome=user["nome"], senha=user["senha"])
    return user

@app.route('/get_user', methods=['GET'])
def get_user():
    return make_response(
        c.search_user()
    ) 

@app.route('/try_login', methods=['POST'])
def try_login():
    user = request.json
    """ 
    TODO
    QUESTÃO DA SEGURANÇA DA REQUISIÇÃO
    """ 
    
    r = c.search_user(where="nome = '{0}' and senha = '{1}'".format(user["nome"], user["senha"]))
    if(len(r) == 1):
        return make_response(
            r
        ) 
    return [None]

@app.route('/set_account', methods=['POST'])
def set_account():
    account = request.json
    print(account)
    c.create_account(bank=account["banco"], typ=account["tipo"], date=account["data"], idUser=account["idUser"], money=account["dinheiro"])
    return account

@app.route('/get_account', methods=['GET', 'POST'])
def get_account():
    try:
        account = request.json
        keys = list(account.keys())
        values = list(account.values())
        print(keys)
        print(values)
        where = ""
        for i in range(len(account)):
            print(keys[i], values[i])
            if(i!=0):
                where= where+"and "
            where = where+"{0} = '{1}' ".format(keys[i], values[i])
        print(where)
        return make_response(
            c.search_account(where=where)
        )
    except:
        return make_response(
            c.search_account()
        ) 


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
        print(keys)
        print(values)
        where = ""
        for i in range(len(routines)):
            print(keys[i], values[i])
            if(i!=0):
                where= where+"and "
            where = where+"{0} = '{1}' ".format(keys[i], values[i])
        print(where)
        return make_response(
            c.search_routines(where=where)
        )
    except:
        return make_response(
            c.search_routines()
        ) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')