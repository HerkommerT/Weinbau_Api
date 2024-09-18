def initialize_routes(app):
    from .index import index_bp
    from .routes import wein_bp,weingut_bp, land_bp, region_bp, rebsorte_bp, typ_bp, art_bp
    
    # Registriere die Blueprints
    app.register_blueprint(index_bp)
    app.register_blueprint(weingut_bp)
    app.register_blueprint(wein_bp)
    app.register_blueprint(land_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(rebsorte_bp)
    app.register_blueprint(typ_bp)
    app.register_blueprint(art_bp)
# Später in app.py könntest du dies verwenden:
# from routes import initialize_routes
# initialize_routes(app)
