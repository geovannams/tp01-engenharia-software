from provasonline import db
from flask_bcrypt import Bcrypt
from provasonline.usuario.models.Usuario import Usuario

######################################################################
#######                         ALUNO                          #######
######################################################################

class Aluno(Usuario): 
	bcrypt = Bcrypt()

	__mapper_args__ = {
		'polymorphic_identity':"aluno"
	}

	__tablename__ = 'aluno'
	id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

	def __init__(self, nome, login, senha, urole):
		self.nome		= nome
		self.login		= login
		self.senha 		= self.setSenha(senha)
		self.urole		= urole


	