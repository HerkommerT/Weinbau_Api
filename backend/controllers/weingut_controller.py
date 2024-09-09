# controllers/weingut_controller.py
from flask import Blueprint, request, jsonify
from models import db, Weingut

weingut_bp = Blueprint('weingut', __name__)

@weingut_bp.route('/add_weingut', methods=['POST'])
def add_weingut():
    data = request.get_json()
    land = data.get('land', '')

    if not land:
        return jsonify({'error': 'Land is required!'}), 400

    weingut = Weingut(land=land)
    try:
        db.session.add(weingut)
        db.session.commit()
        return jsonify({'message': 'Weingut added!', 'weingut_id': weingut.weingut_id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
