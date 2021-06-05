import os
from functools import wraps
from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash, current_app
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os.path import exists

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AGKDGYdsfdfsI874RY9823gsdgdfgYR08Y20sdfwe93287RrewgN2NYORN3827'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir,'storage.db')
# app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:admin@localhost/provasonline'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db, compare_type = True)

#################################################################
################# VARIÁVEIS/FUNÇÕES DO TEMPLATE #################
#################################################################
from provasonline.constants import usuario_urole_roles
@app.context_processor
def insere_usuario_urole_roles():
    return dict(usuario_urole_roles=usuario_urole_roles)

#################################################################
###################### CONFIGURA LOGIN ##########################
#################################################################

login_manager.init_app(app)
login_manager.login_view = "usuario.login"
login_manager.login_message = "Não foi possível acessar esta página ou executar esta ação. Por favor confira se o login foi feito ou se você tem a devida permissão."

def login_required(role=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):

            if not current_user.is_authenticated:
               return current_app.login_manager.unauthorized()
            urole = current_user.urole
            if ((urole not in role) and (role != ["ANY"])):
                flash("Você não tem permissão para acessar essa página.")
                return redirect(url_for('usuario.index'))
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

#################################################################
########################## MODELS ###############################
#################################################################

from provasonline.usuario.models.Usuario import Usuario
from provasonline.aluno.models.Aluno import Aluno
from provasonline.professor.models.Professor import Professor
from provasonline.prova.models.Prova import Prova

#################################################################
########################## BLUEPRINTS ###########################
#################################################################

from provasonline.usuario.routes import usuario
from provasonline.aluno.routes import aluno
from provasonline.professor.routes import professor
from provasonline.prova.routes import prova

app.register_blueprint(usuario, url_prefix='/')
app.register_blueprint(aluno, url_prefix='/aluno')
app.register_blueprint(professor, url_prefix='/professor')
app.register_blueprint(prova, url_prefix='/prova')

