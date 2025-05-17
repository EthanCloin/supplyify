from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object("app.config.Config")

    from app import main
    from app import database

    app.register_blueprint(main.bp)
    with app.app_context():
        database.init_app(app)
    return app
