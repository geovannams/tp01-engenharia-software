from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request

prova = Blueprint('prova', __name__, template_folder='templates')

@prova.route("/cadastrar_prova", methods=["GET","POST"])
def cadastrar_prova():
    return render_template("cadastrar_prova.html")

@prova.route("/listar_provas", methods=["GET","POST"])
def listar_provas():
    return render_template("listar_provas.html")