from flask import Blueprint, request, jsonify
from models import db, Art

art_bp = Blueprint('art', __name__)

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