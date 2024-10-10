# fin.py
from flask import Blueprint, jsonify, request
from models import db, Fin
from extensions import db

# Erstelle den Blueprint
fin_bp = Blueprint('fin', __name__)

# Beispielroute zum Abrufen aller Fin-Einträge
@fin_bp.route('/fins', methods=['GET'])
def get_all_fins():
    fins = Fin.query.all()
    result = [
        {
            "wein_id": fin.wein_id,
            "typ_id": fin.typ_id,
            "art_id": fin.art_id,
            "stückzahl": fin.stückzahl
        }
        for fin in fins
    ]
    return jsonify(result), 200

# Beispielroute zum Erstellen eines neuen Fin-Eintrags
@fin_bp.route('/fins', methods=['POST'])
def create_fin():
    data = request.get_json()
    new_fin = Fin(
        wein_id=data['wein_id'],
        typ_id=data['typ_id'],
        art_id=data['art_id'],
        stückzahl=data['stückzahl']
    )
    db.session.add(new_fin)
    db.session.commit()
    return jsonify({"message": "Fin created successfully!"}), 201
