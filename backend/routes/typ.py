from flask import Blueprint, request, jsonify
from models import db,Typ

typ_bp = Blueprint('typ', __name__)

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