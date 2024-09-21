from extensions import db

class Fin(db.Model):
    __tablename__ = 'absatz'
    
    # Zusammengesetzter Primärschlüssel aus Fremdschlüsseln
    wein_id = db.Column(db.Integer, db.ForeignKey('wein.wein_id'), primary_key=True)
    typ_id = db.Column(db.Integer, db.ForeignKey('typ.typ_id'), primary_key=True)
    art_id = db.Column(db.Integer, db.ForeignKey('art.art_id'), primary_key=True)
    
    # Weitere Attribute
    absatz = db.Column(db.Float, nullable=False)
    
    # Beziehungen
    wein = db.relationship('Wein', backref=db.backref('fins', lazy=True))
    typ = db.relationship('Typ', backref=db.backref('fins', lazy=True))
    art = db.relationship('Art', backref=db.backref('fins', lazy=True))

    def __repr__(self):
        return f'<Fin {self.wein_id}-{self.typ_id}-{self.art_id}>'