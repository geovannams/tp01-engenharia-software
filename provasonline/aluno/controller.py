from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request

aluno = Blueprint('aluno', __name__, template_folder='templates')

@aluno.route("/listar_alunos", methods=["GET","POST"])
def listar_alunos():
    return render_template("listar_alunos.html")