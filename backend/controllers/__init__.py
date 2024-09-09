# controllers/__init__.py

def initialize_controllers(app):
    from .weingut_controller import weingut_bp
    from .wein_controller import wein_bp
    
    # Registriere die Blueprints
    app.register_blueprint(weingut_bp)
    app.register_blueprint(wein_bp)

# Später in app.py könntest du dies verwenden:
# from controllers import initialize_controllers
# initialize_controllers(app)
