from flask import Flask
from flask_migrate import Migrate

from app.data.sqla import sqla


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='secretkey',
        SQLALCHEMY_DATABASE_URI='sqlite:///test_db/test_db.sqlite3',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True
    )

    sqla.init_app(app)

    # Flask-Migrate
    Migrate(app, sqla, render_as_batch=True)

    from app.flask import home_controller, season_controller

    app.register_blueprint(home_controller.blueprint, url_prefix='/home')
    app.register_blueprint(season_controller.blueprint, url_prefix='/seasons')

    app.add_url_rule('/', endpoint='index')

    return app
