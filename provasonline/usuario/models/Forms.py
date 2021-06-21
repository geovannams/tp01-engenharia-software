from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField("login", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired()])
    remember_me = BooleanField("remember_me")

class UsuarioForm(FlaskForm):
	nome = StringField('Nome', validators = [DataRequired()])
	login = StringField('Login', validators = [DataRequired()])
	senha = PasswordField('Senha', validators = [DataRequired()])
	submit = SubmitField('Cadastrar')	