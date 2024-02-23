# IMPORTS
from utils import db
from flask_login import UserMixin
from datetime import datetime
from datetime import date

# TABELAS
class User(db.Model, UserMixin):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))
  tipo = db.Column(db.String(100))
  
  def __init__(self, nome, email, senha, tipo):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.tipo = tipo
 
  def __repr__ (self):
    return f'User: {self.nome}.'

class Amistoso(db.Model):
  __tablename__ = "amistoso"
  id = db.Column(db.Integer, primary_key=True)
  esporte = db.Column(db.String(80))
  curso1 = db.Column(db.String(80))
  curso2 = db.Column(db.String(80))
  Dt_HR = db.Column(db.String(80))
  
  def __init__(self, esporte, curso1, curso2, Dt_HR):
    self.esporte = esporte
    self.curso1 = curso1
    self.curso2 = curso2
    self.Dt_HR = Dt_HR
    
  def __repr__(self):
    return "<Amistoso: {}".format(self.esporte)


