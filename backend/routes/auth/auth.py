from flask import Blueprint, request, session, jsonify
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

# We'll need to pass these as parameters when initializing the blueprint
PASSWORD_HASH = None

# Passwort-Authentifizierung
@auth_bp.route('/auth', methods=['POST'])
def authenticate():
    """Authentifiziert den Benutzer über eine POST-Anfrage mit Passwort"""
    data = request.get_json()
    input_password = data.get('password')

    # Überprüfe, ob das eingegebene Passwort korrekt ist
    if check_password_hash(PASSWORD_HASH, input_password):
        session['authenticated'] = True
        return jsonify({"message": "Authentication successful"}), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401

# Beispiel für eine private Route, die nur nach Authentifizierung zugänglich ist
@auth_bp.route('/private/data', methods=['GET'])
def private_data():
    """Gibt private Daten nur für authentifizierte Benutzer zurück"""
    if session.get('authenticated'):
        # Beispiel für private Daten
        data = {
            "private_info": "This is sensitive data visible to authenticated users."
        }
        return jsonify(data), 200
    else:
        return jsonify({"message": "Unauthorized access"}), 403

def init_auth(password_hash):
    global PASSWORD_HASH
    PASSWORD_HASH = password_hash