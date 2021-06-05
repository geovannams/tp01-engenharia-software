from flask import Blueprint
from provasonline.usuario.controllers.UsuarioController import index, login, logout

usuario = Blueprint('usuario', __name__, template_folder='templates')

usuario.route('/', methods=['GET','POST'])(index)
usuario.route('/login', methods=['GET','POST'])(login)
usuario.route('/logout', methods=['GET','POST'])(logout)