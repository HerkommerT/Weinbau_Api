from flask import Flask, request, jsonify
from models import db, Weingut, Wein
from routes import initialize_routes
from flask_cors import CORS
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3

# Constains Regeln aktivieren, damit Fremdschlüssel Beziehungen funktionieren
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):  # sqlite specific
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'  # Beispiel URI für SQLite
db.init_app(app)

# Initialize CORS with default options (allow all origins)
CORS(app)

initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
