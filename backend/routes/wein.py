# controllers/wein_controller.py
from flask import Blueprint, request, jsonify
from models import db, Wein, Weingut

wein_bp = Blueprint('wein', __name__)

@wein_bp.route('/add_wein', methods=['POST'])
def add_wein():
    data = request.get_json()
    name = data.get('name')
    jahrgang = data.get('jahrgang')
    preis = data.get('preis')
    weingut_id = data.get('weingut_id')

    if not (name and preis and weingut_id):
        return jsonify({'error': 'Name, Preis, and Weingut ID are required'}), 400

    # Optional: Validierung des Jahrgangs und Preises
    if jahrgang and (jahrgang < 0 or preis < 0):
        return jsonify({'error': 'Invalid Jahrgang or Preis'}), 400

    new_wein = Wein(name=name, jahrgang=jahrgang, preis=preis, weingut_id=weingut_id)
    db.session.add(new_wein)
    db.session.commit()

    return jsonify({'message': 'Wein added', 'wein_id': new_wein.wein_id}), 201

@wein_bp.route('/weine', methods=['GET'])
def get_weine():
    try:
        weine = Wein.query.all()
        weine_list = [{
            'wein_id': wein.wein_id,
            'name': wein.name,
            'jahrgang': wein.jahrgang,
            'preis': wein.preis,
            'weingut_id': wein.weingut_id
        } for wein in weine]
        return jsonify(weine_list)
    except Exception as e:
        # Fangen Sie alle Ausnahmen und geben Sie eine Fehlermeldung zurück
        return jsonify({'error': str(e)}), 500