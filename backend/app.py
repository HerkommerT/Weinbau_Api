from flask import Flask, request, jsonify
from models import db, Weingut, Wein

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Beispiel URI für SQLite
db.init_app(app)

@app.route("/")
def index():
    return "<h1>Hello</h1>"

@app.route('/add_weingut', methods=['POST'])
def add_weingut():
    data = request.get_json()
    land = data.get('land')
    
    if not land:
        return jsonify({'error': 'Land is required'}), 400

    new_weingut = Weingut(land=land)
    db.session.add(new_weingut)
    db.session.commit()

    return jsonify({'message': 'Weingut added', 'weingut_id': new_weingut.weingut_id}), 201

@app.route('/add_wein', methods=['POST'])
def add_wein():
    data = request.get_json()
    name = data.get('name')
    jahrgang = data.get('jahrgang')
    preis = data.get('preis')
    weingut_id = data.get('weingut_id')

    if not (name and preis and weingut_id):
        return jsonify({'error': 'Name, Preis, and Weingut ID are required'}), 400

    # Optional: Validierung des Jahrgangs und Preises
    if jahrgang and (jahrgang < 0 or preis < 0):
        return jsonify({'error': 'Invalid Jahrgang or Preis'}), 400

    new_wein = Wein(name=name, jahrgang=jahrgang, preis=preis, weingut_id=weingut_id)
    db.session.add(new_wein)
    db.session.commit()

    return jsonify({'message': 'Wein added', 'wein_id': new_wein.wein_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
