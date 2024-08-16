from flask import Flask, render_template, url_for, redirect, session, request
from dataBase import Connection

app = Flask(__name__)

host_name = "localhost"
user_name = "root"
user_password = "*"
db_name = "Financas"
connect = Connection(host_name, user_name, user_password, db_name)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    if 'nome' in session:
        return render_template("view/home.html", nome=session["nome"])
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('home'))
    return render_template("view/register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('home'))
    return render_template("view/login.html")

@app.post("/cadastrar")
def cadastrar():
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('nome', None)
    return redirect(url_for('home'))

with app.test_request_context():
    print(url_for('home'))
    print(url_for('register'))
    print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
