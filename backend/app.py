from flask import Flask, request, jsonify
from models import db, Weingut, Wein
from routes import initialize_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Beispiel URI für SQLite
db.init_app(app)

initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
