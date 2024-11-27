from main import app
from flask import render_template


@app.route("/")#rota para cadastro
def cadastro():
    return render_template("cadastro.html")

@app.route("/login")#rota para login
def login():
    return render_template("login.html")
