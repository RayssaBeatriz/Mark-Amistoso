# IMPORTS
from flask import jsonify, Blueprint, request
from models import User
from utils import lm, db
from flask_login import login_user, logout_user, login_required, current_user
import hashlib

# CONFIGS
bp_user = Blueprint("bp_user", __name__)

# ROTAS
@bp_user.route('/users', methods=['GET'])
def get_all_users():
  users = User.query.all()
  output = []
  for user in users:
    data = {
      'id': user.id,
      'nome': user.nome,
      'email': user.email,
      'senha': user.senha,
      'tipo' : user.tipo
    }
  
    output.append(data)
  
  response = {
    'status': 'success',
    'users': output,
  }
  
  return jsonify(response), 200


@bp_user.route('/cadastro', methods=['POST'])
def create():
  nome = request.get_json().get('nome')
  email = request.get_json().get('email')
  senha = request.get_json().get('senha')
  tipo = request.get_json().get('tipo')

  new_user = User(nome, email, senha, tipo)
  db.session.add(new_user)
  db.session.commit()

  response = {
    'status': 'success',
    'message': 'Usuario criado!',
  }

  return jsonify(response), 200
  

@bp_user.route('/editar/<int:id>', methods=['PUT'])
def update(id):
  user = User.query.get(id)

  if user:
    user.nome = request.get_json().get('nome')
    user.email = request.get_json().get('email')
    user.senha = request.get_json().get('senha')
    user.tipo = request.get_json().get('tipo')

    db.session.commit()

    response = {
      'status': 'success',
      'message': 'Usuario atualizado!',
    }

    return jsonify(response), 200

  else:
    response = {
        'message': 'Usuario não encontrado :('
    }

    return jsonify(response), 404

@bp_user.route('/desativar/<int:id>', methods=['PUT'])  
def delete(id):
  user = User.query.get(id)
  if user:
    db.session.delete(user)
    db.session.commit()

    response = {
      'status': 'success',
      'message': 'Usuario deletado!',
    }

    return jsonify(response), 200

  else:
    response = {
      'message': 'Usuario não encontrado :('
    }
    return jsonify(response), 404
    
# LOGIN
@bp_user.route('/login', methods=['POST'])
def login():
  email = request.get_json().get('email')
  senha = request.get_json().get('senha')
  
  if senha:
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

  if User.query.filter_by(email = email).filter_by(senha = senha).count() == 1:
    user = User.query.filter_by(email = email).first()
    login_user(user)
    response = {
      'status': 'success',
      'message': 'Usuário logado com sucesso!'
    }
      
    return jsonify(response), 200

  else:
    response = {
      'status': 'success',
      'message': 'Incorrect data!'
    }
      
    return jsonify(response), 200
  
# LOAD
@lm.user_loader
def load_user(id):
  u = User.query.filter_by(id=id).first()
  return u

# LOGOUT
@bp_user.route('/logoff')
def logoff():
  logout_user()
  response = {
    'status': 'success',
    'message': 'Usuário desconectado com sucesso!'
  }

  return jsonify(response), 200
  
