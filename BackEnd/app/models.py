from . import db

class Mae(db.Model):
    __tablename__ = 'mae'
    __table_args__ = {'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.BigInteger)
    idade = db.Column(db.SmallInteger)
    telefone = db.Column(db.BigInteger)
    endereco = db.Column(db.String(100))
    tempo_lactacao = db.Column(db.String(30))
    historico_medico = db.Column(db.String(200))