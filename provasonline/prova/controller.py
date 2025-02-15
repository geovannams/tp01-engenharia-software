from provasonline import db, login_required
from provasonline.prova.models.Prova import Opcao, Pergunta, Prova, Resposta
from provasonline.constants import usuario_urole_roles
from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from datetime import datetime, date

prova = Blueprint('prova', __name__, template_folder='templates')

@prova.route("/cadastrar_prova", methods=["GET","POST"])
# @login_required(role=[usuario_urole_roles['PROFESSOR']])
def cadastrar_prova():
    valor_total = 0

    if request.method == 'POST':

        descricao = request.form['prova']
        data      = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
        #TODO: professor como current_user (preciso do login pronto)
        prova     = Prova(data, descricao, 0, 9)
        db.session.add(prova)
        db.session.commit()

        numero_de_perguntas = request.form['numero_de_perguntas']

        contador = 0

        while (contador < int(numero_de_perguntas)):    
            pergunta = request.form['pergunta'+str(contador)] 
            valor    = request.form['valor'+str(contador)] 

            valor_total = valor_total + int(valor)
            
            questao = Pergunta(pergunta, prova.id, valor)
            db.session.add(questao)    
            db.session.commit()

            opcao1   = request.form['opcao'+str(contador)+'1']
            opcao2   = request.form['opcao'+str(contador)+'2']
            opcao3   = request.form['opcao'+str(contador)+'3']
            opcao4   = request.form['opcao'+str(contador)+'4']   

            correta  = int(request.form['correta'+str(contador)])
            
            alternativa1 = Opcao(opcao1, False, questao.id)
            alternativa2 = Opcao(opcao2, False, questao.id)
            alternativa3 = Opcao(opcao3, False, questao.id)
            alternativa4 = Opcao(opcao4, False, questao.id)

            if (correta == 1):
                alternativa1.correta = True
            elif (correta == 2):
                alternativa2.correta = True
            elif (correta == 3):
                alternativa3.correta = True
            else:        
                alternativa4.correta = True

            db.session.add(alternativa1)
            db.session.add(alternativa2)
            db.session.add(alternativa3)
            db.session.add(alternativa4)                   

            contador = contador + 1    

        prova.valor = valor_total
        
        db.session.commit() 
        flash("Prova cadastrada com sucesso")
        return redirect(url_for('prova.listar_provas'))    

    return render_template("cadastrar_prova.html")

@prova.route("/listar_provas", methods=["GET","POST"])
# @login_required()
def listar_provas():
    #TODO: listar provas do current_user
    #TODO: separar tipo de listagem de aluno e professor

    provas = Prova.query.all()
    return render_template("listar_provas.html", provas = provas)

@prova.route("/responder_prova/<_id>", methods=["GET","POST"])
# @login_required()
def responder_prova(_id):
    prova = Prova.query.get_or_404(_id) 

    #TODO: se ja tiver essa prova respondida pra esse aluno, bloqueia
    #TODO: aluno como current_user (preciso do login pronto)
    #TODO: remover a permissão do botão para o professor

    if request.method == 'POST':
        for p in prova.perguntas: 
            opcao = request.form['op'+str(p.id)]
            
            aux = Opcao.query.get_or_404(opcao)

            if (aux.correta == 1):                
                resposta = Resposta(_id, p.id, opcao, 1, 8)
            else:
                resposta = Resposta(_id, p.id, opcao, 0, 8)

            db.session.add(resposta)    
        db.session.commit()    

        flash("Prova respondida com sucesso!")
        return redirect(url_for('prova.prova_respondida', _id = _id))  

    return render_template("responder_prova.html", prova = prova)

@prova.route("/prova_respondida/<_id>", methods=["GET","POST"])
# @login_required()
def prova_respondida(_id):
    prova = Prova.query.get_or_404(_id)
    respostas = Resposta.query.filter(Resposta.prova == _id).all()
    return render_template("prova_respondida.html", prova = prova, respostas = respostas)