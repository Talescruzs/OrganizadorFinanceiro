from flask import Flask, make_response, request, jsonify
# from dataBase import Connection
from controllers.userController import UserController
from controllers.accountController import AccountController
from controllers.movementController import MovementController
# from controle import verificaUser, verificaAccount

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    try:
        user = request.json
        controller = UserController()
        response = controller.register(name=user["nome"], password=user["senha"], email=user["email"])
        if(response != '0'):
            data = {
                'nome':user["nome"],
                'email':'{0}'.format(user["email"]),
                'hash':'{0}'.format(response)
            }
            return make_response(
                jsonify(
                    user=data
                )
            ) 
        return [None]
    except:
        return [None]

@app.route('/login', methods=['POST'])
def login():
    try:
        user = request.json
        controller = UserController()
        response = controller.login(name=user["nome"], password=user["senha"])
        return make_response(
            jsonify(
                hash=response
            )
        ) 
    except:
        return ["error"]

@app.route('/user', methods=['POST'])
def user():
    try:
        user = request.json
        controller = UserController()
        response = controller.user(name=user["nome"], password=user["senha"], hashCode=user["hash"])
        data = {
            'nome':response['name'],
            'hash':response['hashCode'],
            'email':response['email']
        }
        return make_response(
            jsonify(
                user=data
            )
        ) 
    except:
        return ["error"]

@app.route('/set_account', methods=['POST'])
def set_account():
    try:
        controller = AccountController()
        user = request.json["user"]
        data = request.json["data"]
        response = controller.createAccount(user, data)

        return make_response(
            jsonify(
                status=response
            )
        ) 
    except:
        return ["error"]

@app.route('/get_accounts', methods=['GET', 'POST'])
def get_accounts():
    response = list()

    try:
        userController = UserController()
        user = request.json["user"]
        userAccounts = userController.selectUserAccounts(user)
        accountController = AccountController()

        for r in userAccounts:
            account = accountController.selectAccountById(r[2])
            account['data'] = r[3]
            account['valida'] = r[4]
            response.append(account)

        return make_response(
            response
        )
    except:
        return [None]

@app.route('/delete_account', methods=['DELETE'])
def delete_account():
    try:
        controller = AccountController()
        user = request.json["user"]
        accountId = request.json["data"]["idConta"]
        response = controller.deleteAccountById(user, accountId)

        return make_response(
            jsonify(
                status=response
            )
        ) 
    except:
        return [None]

@app.route('/set_movement', methods=['POST'])
def set_movement():
    # try:
    movController = MovementController()
    accountController = AccountController()

    user = request.json["user"]
    data = request.json["data"]
    response1 = movController.createMovement(user, data)
    response2 = accountController.updateAccountById(user, data)
    response = False
    if(response1 and response2):
        response = True

    return make_response(
        jsonify(
            status=response
        )
    ) 
    # except:
    #     return [None]

@app.route('/get_movements', methods=['POST'])
def get_movements():
    # try:
    movController = MovementController()

    user = request.json["user"]
    accountId = request.json["data"]["idConta"]
    response = movController.selectMovementsByAccount(accountId)

    return make_response(
        jsonify(
            status=response
        )
    ) 
    # except:
    #     return [None]

# @app.route('/set_routines', methods=['POST'])
# def set_routines():
#     routines = request.json
#     print(routines)
#     c.create_routines(typ=routines["tipo"], typR=routines["tipo_r"], value=routines["valor"], iniDate=routines["dataB"], date=routines["data"], desc=routines["desc"], idConta=routines["id_conta"])
#     return routines

# @app.route('/get_routines', methods=['GET', 'POST'])
# def get_routines():
#     try:
#         routines = request.json
#         keys = list(routines.keys())
#         values = list(routines.values())
#         where = ""
#         idUser = c.search_user(where="nome = '{0}' and senha = {1}".format(routines["user"]["nome"], routines["user"]["senha"]))[0][0]
#         accounts = c.search_account(where="id_usuario = {0}".format(idUser))
#         if(len(accounts) == 0):
#             return [None]
#         where = "id_conta in ("
#         for a in range(len(accounts)):
#             if(a!=0):
#                 where+=", "
#             where = where+str(accounts[a][0])
#         where = where+") "
#         for i in range(len(routines)):
#             print(keys[i], values[i])
#             if(keys[i] != "user"):
#                 if(i!=0):
#                     where= where+"and "
#                 where = where+"{0} = '{1}' ".format(keys[i], values[i])
#         print(where)
        
#         return make_response(
#             c.search_routines(where=where)
#         )
#     except:
#         print("fail")
#         return make_response(
#             c.search_routines()
#         ) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')