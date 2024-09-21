from flask import Blueprint, request, jsonify
from models import db, Land

land_bp = Blueprint('land', __name__)

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