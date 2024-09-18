from flask import Blueprint, request, jsonify
from models import db,Region

region_bp = Blueprint('region', __name__)
rebsorte_bp = Blueprint('rebsorte', __name__)
typ_bp = Blueprint('typ', __name__)
art_bp = Blueprint('art', __name__)

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