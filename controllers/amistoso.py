# IMPORTS
from flask import request, jsonify, Blueprint
from utils import db
from models import Amistoso
from datetime import datetime

# CONFIGS
bp_amistoso = Blueprint("bp_amistoso", __name__)

# ROTAS
@bp_amistoso.route('/<int:id>', methods=['GET'])
def get(id):
  amistoso = Amistoso.query.get(id)
  if amistoso:
    data = {
      'id': amistoso.id,
      'esporte': amistoso.esporte,
      'curso1': amistoso.curso1,
      'curso2': amistoso.curso2,
      'Dt_HR': amistoso.Dt_HR
    }
    
    response = {
      'status': 'success',
      'data': data,
    }
    
    return jsonify(response), 200

  else:
    response = {
        'message': 'Amistoso não encontrado :('
    }
    
    return jsonify(response), 404

@bp_amistoso.route('/cadastro', methods=['POST'])
def create():
  esporte = request.get_json().get('esporte')
  curso1 = request.get_json().get('curso1')
  curso2 = request.get_json().get('curso2')
  Dt_HR = request.get_json().get('Dt_HR')

  new_amistoso = Amistoso(esporte=esporte, curso1=curso1, curso2=curso2, Dt_HR=Dt_HR)
  db.session.add(new_amistoso)
  db.session.commit()

  response = {
    'status': 'success',
    'message': 'Amistoso criado!',
  }
    
  return jsonify(response), 200

@bp_amistoso.route('/editar/<int:id>', methods=['PUT'])
def update(id):
  amistoso = Amistoso.query.get(id)
  
  if amistoso:
    amistoso.esporte = request.get_json().get('esporte')
    amistoso.curso1 = request.get_json().get('curso1')
    amistoso.curso2 = request.get_json().get('curso2')
    amistoso.Dt_HR = request.get_json().get('Dt_HR')
    db.session.commit()

    response = {
      'status': 'success',
      'message': 'Amistoso atualizado!',
    }
  
    return jsonify(response), 200

  else:
    response = {
        'message': 'Amistoso não encontrado :('
    }
    
    return jsonify(response), 404
    

@bp_amistoso.route('/desativar/<int:id>', methods=['PUT'])
def delete(id):
  amistoso = Amistoso.query.get(id)
  if amistoso:
    db.session.delete(amistoso)
    db.session.commit()
    
    response = {
    'status': 'success',
    'message': 'Amistoso deletado!',
    }
  
    return jsonify(response), 200
  
  else:
    response = {
        'message': 'Amistoso não encontrado :('
    }
    
    return jsonify(response), 404