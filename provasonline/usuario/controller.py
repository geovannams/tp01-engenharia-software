import os
from provasonline.usuario.models.Usuario import Usuario, load_user
from flask import render_template, request, redirect, url_for, flash
from provasonline import login_required
from flask_login import LoginManager, current_user, login_user, logout_user
from flask import Blueprint
from provasonline.usuario.models.Forms import LoginForm
from flask_bcrypt import Bcrypt
from provasonline import db

usuario = Blueprint('usuario', __name__, template_folder='templates')

######################################################################
######                         INICIO                          #######
######################################################################

@usuario.route('/', methods=['GET','POST'])
# @login_required()
def index():
    return render_template('inicio.html')         
   
######################################################################
########                        LOGIN                          #######
######################################################################

@usuario.route('/login', methods=['GET','POST'])
def login():
    #For GET requests, display the login form. 
    #For POSTS, login the current user by processing the form.
    form = LoginForm()
    if form.validate_on_submit():
        print(form.login.data)
        usuario = load_user(form.login.data)
        if usuario and Bcrypt.check_password_hash(usuario.senha, form.senha.data):
            usuario.authenticated = True
            login_user(usuario, remember=True)
            return redirect(url_for(usuario.inicio))
        else:
            flash("Login inválido.")
    else:
        print(form.errors)
    return render_template('login.html', form=form)
    

######################################################################
########                        LOGOUT                         #######
######################################################################

@usuario.route('/logout', methods=['GET','POST'])
@login_required()
def logout():
    return redirect(url_for('usuario.login'))