# IMPORTS
from flask import Flask, jsonify, session, url_for
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import login_user, logout_user

# CONTROLLERS
from controllers.user import bp_user
from controllers.amistoso import bp_amistoso

# UTILS
from utils import db, lm
from models import User

# CONFIGS
app = Flask(__name__)
app.secret_key = "<markamistoso"
CORS(app, resources={r"/*": {"origins": "*"}})

# BLUEPRINTS
app.register_blueprint(bp_user, url_prefix="/user")
app.register_blueprint(bp_amistoso, url_prefix='/amistoso')

# DATABASE
conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# MIGRATIONS
db.init_app(app)

# MIGRATE'
migrate = Migrate(app, db)

# LOGIN MANAGER
lm.init_app(app)

# ERROR EXCEPTIONS
@app.errorhandler(500)
def all_exception_handler(e):
  response = {
      'message': 'Internal Server Error'
  }
  return jsonify(response), 500

@app.errorhandler(404)
def not_found(e):
  response = {
      'message': 'Pagina nao encontrada'
  }
  return jsonify(response), 404

@app.errorhandler(401)
def unathorized(e):
  response = {
      'message': 'Unauthorized'
  }
  return jsonify(response), 401

app.run(host='0.0.0.0', port=80)