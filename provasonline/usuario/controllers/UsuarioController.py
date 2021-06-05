import os
from flask import render_template, request, redirect, url_for, flash
from provasonline import login_required
from flask_login import LoginManager, current_user, login_user, logout_user

######################################################################
######                         INICIO                          #######
######################################################################

def index():
    if current_user.is_authenticated:
        return render_template('inicio.html')         
    return redirect(url_for('usuario.login')) 
   
######################################################################
########                        LOGIN                          #######
######################################################################

def login():
    return render_template('login.html')

######################################################################
########                        LOGOUT                         #######
######################################################################

@login_required()
def logout():
    return redirect(url_for('usuario.login'))