from marshmallow import (
    Schema,
    fields,
    validates,
    ValidationError
)

class MaeSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=lambda s: len(s)<=50)
    cpf = fields.Int(required=True, validate=lambda s: len(s) ==11)
    idade = fields.Int(required=True, validates=lambda s: len(s) <=120)
    telefone = fields.Int(required=True)
    endereco = fields.Str(required=True, validade=lambda s: len(s) <=100)
    tempo_lactacao = fields.Str(required=True, validate=lambda s: len(s) <=30)
    historico_medico = fields.Str(required=True, validate=lambda s: len(s) <=200)