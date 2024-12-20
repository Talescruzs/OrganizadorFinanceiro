from flask import Flask, render_template, url_for, redirect, session, request
import json  # Import para validar e depurar JSON
import requests
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

url_api = os.getenv('URL_BASE')

# url = "http://192.168.100.10:5000/login"
# json = {
# 	"nome":"Valquiria",
# 	"senha":"1234"
# }

# response = requests.post(url=url, json=json)
# print(response.json())

app = Flask(__name__)

# host_name = "localhost"
# user_name = "root"
# user_password = "*"
# db_name = "Financas"
# connect = Connection(host_name, user_name, user_password, db_name)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def home():
    if 'user' in session:
        print(session['user'])
        return render_template("home.html", nome=session["user"]["nome"])
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        url = "{0}/register".format(url_api)
        json = {
            "nome":request.form['nome'],
            "senha":request.form['senha'],
            "email":request.form['email']
        }
        response = requests.post(url=url, json=json)
        session['user'] = response.json()["user"]
        return redirect(url_for('home'))
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        url = "{0}/login".format(url_api)
        json = {
            "nome":request.form['nome'],
            "senha":request.form['senha']
        }
        response = requests.post(url=url, json=json)
        if(response.json() != [None]):
            session['user'] = response.json()["user"]
            return redirect(url_for('home'))
        return render_template("login.html", alerta="Errado, tente novamente")
    return render_template("login.html")

@app.route('/logout', methods=['GET'])
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route("/contas", methods=['GET'])
def contas():
    if 'user' not in session:
        return redirect(url_for('login'))

    url = "{0}/get_accounts".format(url_api)
    json = {
        "user":session['user']
    }
    response = requests.post(url=url, json=json)
    print(response.json())


    return render_template("contas.html", contas=response.json())

@app.route("/contas/criar", methods=['GET', 'POST'])
def criarConta():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        url = f"{url_api}/set_account"
        payload = {
            "user": {
                "email": session['user']['email'],
                "hash": session['user']['hash'],
                "nome": session['user']['nome']
            },
            "data": {
                "nomeBanco": request.form['banco'].strip(),
                "tipoConta": request.form['tipo'].strip().upper(),
                "valor": int(request.form['dinheiro'])
            }
        }

        # Validar JSON antes de enviar
        try:
            json_payload = json.dumps(payload)  # Validação de formato JSON
            print("Payload JSON válido:", json_payload)
        except Exception as e:
            print("Erro ao validar JSON:", e)
            return "Erro na estrutura do payload"

        # Enviar a requisição
        response = requests.post(url=url, json=payload)

        # Logar a resposta para depuração
        try:
            print("Resposta da API:", response.status_code, response.json())
        except Exception as e:
            print("Erro ao processar a resposta da API:", e)
            print("Texto bruto da resposta:", response.text)

        return redirect(url_for('contas'))


    return render_template("criarContas.html")

@app.route("/contas/deleta<int:conta_id>", methods=['POST'])
def deletaConta(conta_id):
    return redirect(url_for('contas'))
    # if 'user' not in session:
    #     return redirect(url_for('login'))

    # url = "{0}/delete_account".format(url_api)
    # json = {
    #     "user":session['user'],
    #     "data":{
    #         "id":conta_id
    #     }
    # }
    # response = requests.delete(url=url, json=json)
    # print(response.json())
    # return redirect(url_for('contas'))

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
