from flask import Flask, render_template, url_for, redirect, session, request
# from dataBase import Connection
import requests
from dotenv import load_dotenv
from pathlib import Path
import os

try:
    dotenv_path = Path('./.env')
    load_dotenv(dotenv_path=dotenv_path)
except:
    pass

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

@app.route("/")
def home():
    if 'user' in session:
        return render_template("view/home.html", nome=session["user"]["nome"])
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        url = "{0}/register".format(url_api)
        json = {
            "nome":request.form['nome'],
            "senha":request.form['senha']
        }
        response = requests.post(url=url, json=json)
        session['user'] = response.json()["user"]
        return redirect(url_for('home'))
    return render_template("view/register.html")

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
        return render_template("view/login.html", alerta="Errado, tente novamente")
    return render_template("view/login.html")

@app.post("/cadastrar")
def cadastrar():
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('home'))

with app.test_request_context():
    print(url_for('home'))
    print(url_for('register'))
    print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
