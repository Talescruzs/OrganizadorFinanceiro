from flask import Flask, make_response, request
from dataBase import Connection

host_name = "localhost"
user_name = "root"
user_password = "*"
db_name = "Financas"
c = Connection(host_name, user_name, user_password, db_name)
# c.create_user(nome="Teste", senha="123")

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def set_user():
    user = request.json
    return user

@app.route('/register', methods=['GET'])
def get_user():
    return make_response(
        c.search_user()
    ) 

# @app.route('/register')
# def get_user():
#     return make_response(
#         c.search_user()
#     ) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')