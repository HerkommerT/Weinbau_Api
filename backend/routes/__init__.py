def initialize_routes(app, password_hash):
    from .wein.index import index_bp
    from .wein.wein import wein_bp
    from .wein.weingut import weingut_bp
    from .wein.land import land_bp
    from .wein.region import region_bp
    from .wein.rebsorte import rebsorte_bp
    from .wein.typ import typ_bp
    from .wein.art import art_bp
    from .wein.fin import fin_bp
    from .auth.auth import auth_bp, init_auth
    
    init_auth(password_hash)
    
    # Registriere die Blueprints
    app.register_blueprint(index_bp)
    app.register_blueprint(weingut_bp)
    app.register_blueprint(wein_bp)
    app.register_blueprint(land_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(rebsorte_bp)
    app.register_blueprint(typ_bp)
    app.register_blueprint(art_bp)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(fin_bp) 
# Später in app.py könntest du dies verwenden:
# from routes import initialize_routes
# initialize_routes(app)
