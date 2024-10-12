# fin.py
from flask import Blueprint, jsonify, request, session
from models import db, Fin
from sqlalchemy.orm import joinedload
from extensions import db

# Erstelle den Blueprint
fin_bp = Blueprint('fin', __name__)

# Route zum Abrufen aller Fin-Einträge, jetzt unter /private/fins
@fin_bp.route('/private/fins', methods=['GET'])
def get_all_fins():
    if session.get('authenticated'):
        fins = Fin.query.options(joinedload(Fin.wein)).all()
        
        # Berechnung des Absatzes und Hinzufügen zur Liste
        result = [
            {
                'id': fin.id,
                'wein_id': fin.wein_id,
                'typ_id': fin.typ_id,
                'art_id': fin.art_id,
                'stückzahl': fin.stückzahl,
                'preis': fin.wein.preis if fin.wein else None,  # Preis des Weins über die Beziehung
                'absatz': (fin.stückzahl * fin.wein.preis) if fin.wein else 0  # Berechnung des Absatzes
            }
            for fin in fins
        ]
        
        return jsonify(result), 200
    else:
        return jsonify({"message": "Unauthorized access"}), 403

# Route zum Erstellen eines neuen Fin-Eintrags, jetzt unter /private/fins
@fin_bp.route('/private/fins', methods=['POST'])
def create_fin():
    if session.get('authenticated'):
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
    else:
        return jsonify({"message": "Unauthorized access"}), 403