from provasonline import db

class Turma(db.Model):

    __tablename__ = 'turma'
    id = db.Column(db.Integer, primary_key = True)

    def __init__(self):
        pass