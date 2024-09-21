from flask import Flask
from models import db
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from sqlalchemy import event
from sqlalchemy.engine import Engine
import os
import sqlite3

# Setze das Standardpasswort
PASSWORD_HASH = generate_password_hash('admin')

# Constains Regeln aktivieren, damit Fremdschlüssel Beziehungen funktionieren
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):  # sqlite specific
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'  # Beispiel URI für SQLite
    app.config['SECRET_KEY'] = os.urandom(24)  # Zum Signieren der Sitzungen
    db.init_app(app)

    # Initialize CORS with default options (allow all origins)
    CORS(app)

    # Import and register blueprints
    from routes import initialize_routes
    initialize_routes(app, PASSWORD_HASH)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)