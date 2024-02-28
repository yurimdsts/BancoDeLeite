from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seu_usuario:senha@localhost/BancoDeLeite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para a tabela Funcionarios
class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.SmallInteger)
    endereco = db.Column(db.String(100))
    CPF = db.Column(db.BigInteger)
    cargo = db.Column(db.String(20))

# Modelo para a tabela Mae
class Mae(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    CPF = db.Column(db.BigInteger)
    idade = db.Column(db.SmallInteger)
    telefone = db.Column(db.BigInteger)
    endereco = db.Column(db.String(100))
    tempo_lactacao = db.Column(db.String(30))
    historico_medico = db.Column(db.String(200))

# Modelo para a tabela Leite
class Leite(db.Model):
    id_lote = db.Column(db.Integer, primary_key=True)
    qualidade = db.Column(db.String(20))
    estado = db.Column(db.String(20))
    distribuicao = db.Column(db.String(15))
    validade = db.Column(db.Integer)

# Rotas da Web API

@app.route('/funcionarios', methods=['GET'])
def get_all_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([funcionario.__dict__ for funcionario in funcionarios])

@app.route('/funcionarios/<int:funcionario_id>', methods=['GET'])
def get_funcionario(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
    if funcionario:
        return jsonify(funcionario.__dict__)
    return jsonify({'message': 'Funcionário não encontrado'}), 404

@app.route('/funcionarios', methods=['POST'])
def add_funcionario():
    data = request.get_json()
    new_funcionario = Funcionario(**data)
    db.session.add(new_funcionario)
    db.session.commit()
    return jsonify(new_funcionario.__dict__), 201

# Rotas semelhantes para as tabelas Mae e Leite...

if __name__ == '__main__':
    # Criar as tabelas no banco de dados antes de iniciar a aplicação
    db.create_all()
    app.run(debug=True)
