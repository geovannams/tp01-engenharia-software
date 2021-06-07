from provasonline import db, login_required
from provasonline.prova.models.Prova import Pergunta, Prova
from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from datetime import datetime, date

prova = Blueprint('prova', __name__, template_folder='templates')

@prova.route("/cadastrar_prova", methods=["GET","POST"])
def cadastrar_prova():
    # if request.method == 'POST':

    #     descricao = request.form['prova']
    #     data      = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
    #     total     = request.form['total']
    #     prova     = Prova(data, descricao, total)
    #     db.session.add(prova)
    #     db.session.commit()

    #     numero_de_perguntas = request.form['numero_de_perguntas']

    #     contador = 0

    #     while (contador < int(numero_de_perguntas)):           
    #         pergunta = request.form['pergunta'+contador]
    #         valor    = request.form['valor'+contador]
    #         opcao1   = request.form['opcao'+contador+'1']
    #         opcao2   = request.form['opcao'+contador+'2']
    #         opcao3   = request.form['opcao'+contador+'3']
    #         opcao4   = request.form['opcao'+contador+'4']

    return render_template("cadastrar_prova.html")

@prova.route("/listar_provas", methods=["GET","POST"])
def listar_provas():
    return render_template("listar_provas.html")