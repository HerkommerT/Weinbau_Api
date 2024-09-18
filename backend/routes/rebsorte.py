from flask import Blueprint, request, jsonify
from models import db, Rebsorte

rebsorte_bp = Blueprint('rebsorte', __name__)

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