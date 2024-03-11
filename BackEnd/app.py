from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, '../FrontEnd/templates'), 
            static_folder=os.path.join(BASE_DIR, '../FrontEnd/static'))


# Configurações do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://npzjffcr:Sl_8yHVcyM0pRrBiuL2IuJKamSRginyx@kesavan.db.elephantsql.com/npzjffcr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para a tabela Funcionarios
# class Funcionario(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(50), nullable=False)
#     idade = db.Column(db.SmallInteger)
#     endereco = db.Column(db.String(100))
#     CPF = db.Column(db.BigInteger)
#     cargo = db.Column(db.String(20))

# Modelo para a tabela Mae
class Mae(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.BigInteger)
    idade = db.Column(db.SmallInteger)
    telefone = db.Column(db.BigInteger)
    endereco = db.Column(db.String(100))
    tempo_lactacao = db.Column(db.String(30))
    historico_medico = db.Column(db.String(200))

# Modelo para a tabela Leite
# class Leite(db.Model):
#     id_lote = db.Column(db.Integer, primary_key=True)
#     qualidade = db.Column(db.String(20))
#     estado = db.Column(db.String(20))
#     distribuicao = db.Column(db.String(15))
#     validade = db.Column(db.Integer)

# Rotas da Web API

# @app.route('/funcionarios', methods=['GET'])
# def get_all_funcionarios():
#     funcionarios = Funcionario.query.all()
#     return jsonify([funcionario.__dict__ for funcionario in funcionarios])

# @app.route('/funcionarios/<int:funcionario_id>', methods=['GET'])
# def get_funcionario(funcionario_id):
#     funcionario = Funcionario.query.get(funcionario_id)
#     if funcionario:
#         return jsonify(funcionario.__dict__)
#     return jsonify({'message': 'Funcionário não encontrado'}), 404

# @app.route('/funcionarios', methods=['POST'])
# def add_funcionario():
#     data = request.get_json()
#     new_funcionario = Funcionario(**data)
#     db.session.add(new_funcionario)
#     db.session.commit()
#     return jsonify(new_funcionario.__dict__), 201

@app.route('/cadastro_mae', methods = ['GET','POST'])
def cadastro_mae():
    if request.method == 'GET':
        return render_template('cadastro_mae.html')
    else:
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        idade = request.form.get('idade')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        tempo_lactacao = request.form.get('tempo_lactacao')
        historico_medico = request.form.get('historico_medico')    


        if len (nome) > 50:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        if len (cpf) > 11:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        if len (idade) > 120:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        if len (endereco) > 100:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        if len (tempo_lactacao) > 30:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        if len (historico_medico) > 200:
            return jsonify ({'error': 'limite de caracteres atingido'}),400
        
        nova_mae=Mae(
            nome = nome,
            cpf = cpf,
            idade = idade,
            telefone = telefone,
            endereco = endereco,
            tempo_lactacao = tempo_lactacao,
            historico_medico = historico_medico,
        ) 

        db.session.add(nova_mae)
        try:
            db.session.commit()
            return jsonify ({'message': 'dados salvos'}),201
        except Exception as e:
            db.session.rollback()
            return jsonify ({'error' : str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')        
# Rotas semelhantes para as tabelas Mae e Leite...

if __name__ == '__main__':
    # Criar as tabelas no banco de dados antes de iniciar a aplicação
    with app.app_context():
        db.create_all()
    app.run(debug=True)
