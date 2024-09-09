def initialize_routes(app):
    from .weingut import weingut_bp
    from .wein import wein_bp
    from .index import index_bp
    
    # Registriere die Blueprints
    app.register_blueprint(weingut_bp)
    app.register_blueprint(wein_bp)
    app.register_blueprint(index_bp)

# Später in app.py könntest du dies verwenden:
# from routes import initialize_routes
# initialize_routes(app)
