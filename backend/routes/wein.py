from flask import Blueprint, request, jsonify
from models import db, Wein

wein_bp = Blueprint('wein', __name__)

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