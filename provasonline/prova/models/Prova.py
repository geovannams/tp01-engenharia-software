from provasonline import db

class Prova(db.Model):

    __tablename__ = 'prova'
    id          = db.Column(db.Integer, primary_key = True)
    descricao   = db.Column(db.Text, nullable = True)
    data        = db.Column(db.Date, nullable = False)
    
    def __init__(self, data, descricao):
        self.data      = data
        self.descricao = descricao


class Pergunta(db.Model):

    __tablename__ = 'pergunta'
    id          = db.Column(db.Integer, primary_key = True)
    descricao   = db.Column(db.Text, nullable = False)
    prova       = db.Column(db.Integer, db.ForeignKey('prova.id', ondelete = 'CASCADE'), nullable = False)
    
    def __init__(self, descricao, prova):
        self.descricao = descricao
        self.prova     = prova

class Opcao(db.Model):

    __tablename__ = 'opcao'
    id          = db.Column(db.Integer, primary_key = True)
    descricao   = db.Column(db.Text, nullable = False)
    correta     = db.Column(db.Boolean, nullable = False)
    pergunta    = db.Column(db.Integer, db.ForeignKey('pergunta.id', ondelete = 'CASCADE'), nullable = False)
    
    def __init__(self, descricao, correta, pergunta):
        self.descricao = descricao
        self.correta   = correta
        self.pergunta  = pergunta

class Resposta(db.Model):

    __tablename__ = 'resposta'
    id         = db.Column(db.Integer, primary_key = True)
    pergunta   = db.Column(db.Integer, db.ForeignKey('pergunta.id', ondelete = 'CASCADE'), nullable = False)
    opcao      = db.Column(db.Integer, db.ForeignKey('opcao.id', ondelete = 'CASCADE'), nullable = False)
    # aluno      = db.Column(db.Integer, db.ForeignKey('aluno.id', ondelete = 'CASCADE'), nullable = False)
    
    def __init__(self, pergunta, opcao): # , aluno
        self.pergunta = pergunta
        self.opcao    = opcao
        # self.aluno    = aluno
