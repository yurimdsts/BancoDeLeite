from flask import (
    Blueprint,
    request,
    jsonify,
    render_template
)
from .models import Mae
from .schemas import MaeSchema
from . import db
from marshmallow import ValidationError
main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template("index.html")        

@main.route('/cadastro_mae', methods = ['GET','POST'])
def cadastro_mae():
    if request.method == 'GET':
        return render_template('cadastro_mae.html')
    else:
        mae_schema = MaeSchema()
        try:
            data = mae_schema.load(request.form)
        except ValidationError as e:
            return jsonify(e.messages), 400
        nova_mae = Mae(**data)
        db.session.add(nova_mae)
        try:
            db.session.commit()
            return jsonify (mae_schema.dump(nova_mae)),201
        except Exception as e:
            db.session.rollback()
            return jsonify ({'error' : str(e)}), 500
