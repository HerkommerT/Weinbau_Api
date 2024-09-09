# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weingut(db.Model):
    __tablename__ = 'weingut'
    weingut_id = db.Column(db.Integer, primary_key=True)
    land = db.Column(db.String(100), nullable=False)

    # Beziehung zu Wein (1:n)
    weine = db.relationship('Wein', backref='weingut', lazy=True)

class Wein(db.Model):
    __tablename__ = 'wein'
    wein_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    jahrgang = db.Column(db.Integer)
    preis = db.Column(db.Float, nullable=False)
    weingut_id = db.Column(db.Integer, db.ForeignKey('weingut.weingut_id'), nullable=False)
