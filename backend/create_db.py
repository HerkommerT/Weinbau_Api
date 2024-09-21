from app import create_app, db  # Importiere die Funktion, um die App und das Datenbankobjekt zu erstellen

# Erstelle eine neue App-Instanz
app = create_app()

# Initialisiere die Datenbank und erstelle die Tabellen
with app.app_context():  # Stelle sicher, dass du im Anwendungskontext arbeitest
    db.create_all()  # Erstelle alle Tabellen in der Datenbank
    print("Datenbanktabellen wurden erstellt.")
