from extensions import db

class Land(db.Model):
    __tablename__ = 'land'
    land_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Beziehung zu Regionen (1:n)
    regionen = db.relationship('Region', backref='land', lazy=True)


class Region(db.Model):
    __tablename__ = 'region'
    region_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    beschr = db.Column(db.String(255))
    land_id = db.Column(db.Integer, db.ForeignKey('land.land_id'), nullable=False)

    # Beziehung zu Weingütern (1:n)
    weinguter = db.relationship('Weingut', backref='region', lazy=True)


class Weingut(db.Model):
    __tablename__ = 'weingut'
    weingut_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.region_id'), nullable=False)

    # Beziehung zu Weinen (1:n)
    weine = db.relationship('Wein', backref='weingut', lazy=True)


class Rebsorte(db.Model):
    __tablename__ = 'rebsorte'
    sort_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Viele-zu-Viele Beziehung zu Weinen über Wein_Rebsorte
    weine = db.relationship('Wein_Rebsorte', backref='rebsorte', lazy=True)


class Wein_Rebsorte(db.Model):
    __tablename__ = 'wein_rebsorte'
    wein_id = db.Column(db.Integer, db.ForeignKey('wein.wein_id'), primary_key=True)
    sort_id = db.Column(db.Integer, db.ForeignKey('rebsorte.sort_id'), primary_key=True)


class Wein(db.Model):
    __tablename__ = 'wein'
    wein_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    jahrgang = db.Column(db.Integer)
    beschr = db.Column(db.String(255))
    preis = db.Column(db.Float, nullable=False)
    weingut_id = db.Column(db.Integer, db.ForeignKey('weingut.weingut_id'), nullable=False)
    typ_id = db.Column(db.Integer, db.ForeignKey('typ.typ_id'), nullable=False)
    art_id = db.Column(db.Integer, db.ForeignKey('art.art_id'), nullable=False)

    # Viele-zu-Viele Beziehung zu Rebsorten über Wein_Rebsorte
    rebsorten = db.relationship('Wein_Rebsorte', backref='wein', lazy=True)


class Typ(db.Model):
    __tablename__ = 'typ'
    typ_id = db.Column(db.Integer, primary_key=True)
    bez = db.Column(db.String(100), nullable=False)

    # Beziehung zu Weinen (1:n)
    weine = db.relationship('Wein', backref='typ', lazy=True)


class Art(db.Model):
    __tablename__ = 'art'
    art_id = db.Column(db.Integer, primary_key=True)
    bez = db.Column(db.String(100), nullable=False)

    # Beziehung zu Weinen (1:n)
    weine = db.relationship('Wein', backref='art', lazy=True)
