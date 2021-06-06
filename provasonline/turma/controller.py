from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request

turma = Blueprint('turma', __name__, template_folder='templates')

@turma.route("/listar_turmas", methods=["GET","POST"])
def listar_turmas():
    return render_template("listar_turmas.html")