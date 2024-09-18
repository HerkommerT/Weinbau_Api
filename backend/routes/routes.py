from flask import Blueprint, request, jsonify
from models import db, Wein, Weingut, Land, Region, Rebsorte, Typ, Art

wein_bp = Blueprint('wein', __name__)
weingut_bp = Blueprint('weingut', __name__)
land_bp = Blueprint('land', __name__)
region_bp = Blueprint('region', __name__)
rebsorte_bp = Blueprint('rebsorte', __name__)
typ_bp = Blueprint('typ', __name__)
art_bp = Blueprint('art', __name__)

# CRUD-Routen für Wein
@wein_bp.route('/wein', methods=['POST'])
def add_wein():
    data = request.get_json()
    name = data.get('name')
    jahrgang = data.get('jahrgang')
    beschr = data.get('beschr')
    preis = data.get('preis')
    weingut_id = data.get('weingut_id')
    typ_id = data.get('typ_id')
    art_id = data.get('art_id')

    # Validierung: Name, Preis, Weingut ID, Typ ID und Art ID sind erforderlich
    if not (name and preis and weingut_id and typ_id and art_id):
        return jsonify({'error': 'Name, Preis, Weingut ID, Typ ID, and Art ID are required'}), 400

    # Optional: Validierung des Jahrgangs und Preises
    if jahrgang and (jahrgang < 0 or preis < 0):
        return jsonify({'error': 'Invalid Jahrgang or Preis'}), 400

    new_wein = Wein(
        name=name,
        jahrgang=jahrgang,
        beschr=beschr,
        preis=preis,
        weingut_id=weingut_id,
        typ_id=typ_id,
        art_id=art_id
    )
    db.session.add(new_wein)
    db.session.commit()

    return jsonify({'message': 'Wein added', 'wein_id': new_wein.wein_id}), 201


@wein_bp.route('/wein', methods=['GET'])
def get_weine():
    weine = Wein.query.all()
    weine_list = [{
        'wein_id': wein.wein_id,
        'name': wein.name,
        'jahrgang': wein.jahrgang,
        'beschr': wein.beschr,
        'preis': wein.preis,
        'weingut_id': wein.weingut_id,
        'typ_id': wein.typ_id,
        'art_id': wein.art_id
    } for wein in weine]
    return jsonify(weine_list)


@wein_bp.route('/wein/<int:wein_id>', methods=['GET'])
def get_wein(wein_id):
    wein = Wein.query.get_or_404(wein_id)
    return jsonify({
        'wein_id': wein.wein_id,
        'name': wein.name,
        'jahrgang': wein.jahrgang,
        'beschr': wein.beschr,
        'preis': wein.preis,
        'weingut_id': wein.weingut_id,
        'typ_id': wein.typ_id,
        'art_id': wein.art_id
    })

# CRUD-Routen für Weingut
@weingut_bp.route('/weingut', methods=['POST'])
def add_weingut():
    data = request.get_json()
    name = data.get('name')
    region_id = data.get('region_id')

    if not name or not region_id:
        return jsonify({'error': 'Name and Region ID are required'}), 400

    new_weingut = Weingut(name=name, region_id=region_id)
    db.session.add(new_weingut)
    db.session.commit()

    return jsonify({'message': 'Weingut added', 'weingut_id': new_weingut.weingut_id}), 201

@weingut_bp.route('/weingut', methods=['GET'])
def get_weinguter():
    weinguter = Weingut.query.all()
    weinguter_list = [{
        'weingut_id': weingut.weingut_id,
        'name': weingut.name,
        'region_id': weingut.region_id
    } for weingut in weinguter]
    return jsonify(weinguter_list)

@weingut_bp.route('/weingut/<int:weingut_id>', methods=['GET'])
def get_weingut(weingut_id):
    weingut = Weingut.query.get_or_404(weingut_id)
    return jsonify({
        'weingut_id': weingut.weingut_id,
        'name': weingut.name,
        'region_id': weingut.region_id
    })

@weingut_bp.route('/weingut/<int:weingut_id>', methods=['DELETE'])
def delete_weingut(weingut_id):
    weingut = Weingut.query.get_or_404(weingut_id)
    db.session.delete(weingut)
    db.session.commit()
    return jsonify({'message': 'Weingut deleted'})

# CRUD-Routen für Land
@land_bp.route('/land', methods=['POST'])
def add_land():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_land = Land(name=name)
    db.session.add(new_land)
    db.session.commit()

    return jsonify({'message': 'Land added', 'land_id': new_land.land_id}), 201

@land_bp.route('/land', methods=['GET'])
def get_lands():
    lands = Land.query.all()
    land_list = [{'land_id': land.land_id, 'name': land.name} for land in lands]
    return jsonify(land_list)

# CRUD-Routen für Region
@region_bp.route('/region', methods=['POST'])
def add_region():
    data = request.get_json()
    name = data.get('name')
    beschr = data.get('beschr')
    land_id = data.get('land_id')

    if not name or not land_id:
        return jsonify({'error': 'Name and Land ID are required'}), 400

    new_region = Region(name=name, beschr=beschr, land_id=land_id)
    db.session.add(new_region)
    db.session.commit()

    return jsonify({'message': 'Region added', 'region_id': new_region.region_id}), 201

@region_bp.route('/region', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    region_list = [{
        'region_id': region.region_id,
        'name': region.name,
        'beschr': region.beschr,
        'land_id': region.land_id
    } for region in regions]
    return jsonify(region_list)

# CRUD-Routen für Rebsorte
@rebsorte_bp.route('/rebsorte', methods=['POST'])
def add_rebsorte():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_rebsorte = Rebsorte(name=name)
    db.session.add(new_rebsorte)
    db.session.commit()

    return jsonify({'message': 'Rebsorte added', 'rebsorte_id': new_rebsorte.sort_id}), 201

@rebsorte_bp.route('/rebsorte', methods=['GET'])
def get_rebsorten():
    rebsorten = Rebsorte.query.all()
    rebsorten_list = [{'sort_id': rebsorte.sort_id, 'name': rebsorte.name} for rebsorte in rebsorten]
    return jsonify(rebsorten_list)

# CRUD-Routen für Typ
@typ_bp.route('/typ', methods=['POST'])
def add_typ():
    data = request.get_json()
    bez = data.get('bez')

    if not bez:
        return jsonify({'error': 'Bez is required'}), 400

    new_typ = Typ(bez=bez)
    db.session.add(new_typ)
    db.session.commit()

    return jsonify({'message': 'Typ added', 'typ_id': new_typ.typ_id}), 201

@typ_bp.route('/typ', methods=['GET'])
def get_typen():
    typen = Typ.query.all()
    typen_list = [{'typ_id': typ.typ_id, 'bez': typ.bez} for typ in typen]
    return jsonify(typen_list)

# CRUD-Routen für Art
@art_bp.route('/art', methods=['POST'])
def add_art():
    data = request.get_json()
    bez = data.get('bez')

    if not bez:
        return jsonify({'error': 'Bez is required'}), 400

    new_art = Art(bez=bez)
    db.session.add(new_art)
    db.session.commit()

    return jsonify({'message': 'Art added', 'art_id': new_art.art_id}), 201

@art_bp.route('/art', methods=['GET'])
def get_arten():
    arten = Art.query.all() 
    arten_list = [{'art_id': art.art_id, 'bez': art.bez} for art in arten]
    return jsonify(arten_list)