from app import app, db  # Importiere die Flask-Anwendung und das Datenbankobjekt

with app.app_context():  # Stelle sicher, dass du im Anwendungskontext arbeitest
    db.create_all()  # Erstelle alle Tabellen
    print("Datenbanktabellen wurden erstellt.")
