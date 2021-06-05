import os
from flask import render_template, request, redirect, url_for, flash
from provasonline import login_required
from flask_login import LoginManager, current_user, login_user, logout_user
from flask import Blueprint

usuario = Blueprint('usuario', __name__, template_folder='templates')

######################################################################
######                         INICIO                          #######
######################################################################

@usuario.route('/', methods=['GET','POST'])
@login_required()
def index():
    return render_template('inicio.html')         
   
######################################################################
########                        LOGIN                          #######
######################################################################

@usuario.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

######################################################################
########                        LOGOUT                         #######
######################################################################

@usuario.route('/logout', methods=['GET','POST'])
@login_required()
def logout():
    return redirect(url_for('usuario.login'))