from extensions import db

class Fin(db.Model):
    __tablename__ = 'absatz'
    
    # Auto increment, not null, primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Fremdschlüssel
    wein_id = db.Column(db.Integer, db.ForeignKey('wein.wein_id'), nullable=False)
    typ_id = db.Column(db.Integer, db.ForeignKey('typ.typ_id'), nullable=False)
    art_id = db.Column(db.Integer, db.ForeignKey('art.art_id'), nullable=False)
    
    # Weitere Attribute
    stückzahl = db.Column(db.Integer, nullable=False)
    
    # Beziehungen
    wein = db.relationship('Wein', backref=db.backref('fins', lazy=True))
    typ = db.relationship('Typ', backref=db.backref('fins', lazy=True))
    art = db.relationship('Art', backref=db.backref('fins', lazy=True))

    def __repr__(self):
        return f'<Fin {self.id}: {self.wein_id}-{self.typ_id}-{self.art_id}>'