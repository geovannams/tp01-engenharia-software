import os
from provasonline.usuario.models.Usuario import Usuario
from flask import render_template, request, redirect, url_for, flash
from provasonline import login_required
from flask_login import LoginManager, current_user, login_user, logout_user
from flask import Blueprint
from provasonline.usuario.models.Forms import LoginForm
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
    # if form.validate_on_submit():
    #     user = Usuario.query.get(form.email.data)
    #     if user:
    #         if bcrypt.check_password_hash(user.password, form.password.data):
    #             user.authenticated = True
    #             db.session.add(user)
    #             db.session.commit()
    #             login_user(user, remember=True)
    #             return redirect(url_for("inicio.html"))
    return render_template("login.html", form=form)
    

######################################################################
########                        LOGOUT                         #######
######################################################################

@usuario.route('/logout', methods=['GET','POST'])
@login_required()
def logout():
    return redirect(url_for('usuario.login'))