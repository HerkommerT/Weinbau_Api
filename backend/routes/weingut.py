from flask import Blueprint, request, jsonify
from models import db, Weingut

weingut_bp = Blueprint('weingut', __name__)

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