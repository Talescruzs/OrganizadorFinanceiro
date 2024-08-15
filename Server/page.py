from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("view/home.html")

@app.route("/register")
def register():
    return render_template("view/register.html")

@app.route("/login")
def login():
    return render_template("view/login.html")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
