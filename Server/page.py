from flask import Flask, render_template, url_for, redirect
from dataBase import Connection

app = Flask(__name__)

host_name = "localhost"
user_name = "root"
user_password = "*"
db_name = "Financas"
connect = Connection(host_name, user_name, user_password, db_name)

@app.route("/")
def home():
    return render_template("view/home.html")

@app.route("/register")
def register():
    return render_template("view/register.html", connect = connect)

@app.route("/login")
def login():
    return render_template("view/login.html", methods=['GET', 'POST'])

@app.post("/cadastrar")
def cadastrar():
    return redirect(url_for('home'))

with app.test_request_context():
    print(url_for('home'))
    print(url_for('register'))
    print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
