def initialize_routes(app):
    from .index import index_bp
    from .wein import wein_bp
    from .weingut import weingut_bp
    from .land import land_bp
    from .region import region_bp
    from .rebsorte import rebsorte_bp
    from .typ import typ_bp
    from .art import art_bp
    
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
