# controllers/wein_controller.py
from flask import Blueprint, request, jsonify
from models import db, Wein, Weingut

wein_bp = Blueprint('wein', __name__)

@wein_bp.route('/add_wein', methods=['POST'])
def add_wein():
    data = request.get_json()
    weingut = Weingut.query.get(data['weingut_id'])
    if not weingut:
        return jsonify({'message': 'Weingut not found!'}), 404
    
    wein = Wein(name=data['name'], preis=data['preis'], weingut_id=data['weingut_id'])
    db.session.add(wein)
    db.session.commit()
    return jsonify({'message': 'Wein added!', 'wein_id': wein.wein_id})
