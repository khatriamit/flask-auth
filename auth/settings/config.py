from flask import Flask
from entrypoints.routes import auth_routes
from model.database import db


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    if test_config is None:
        print("hellos")
        app.config.from_mapping(
            SECRET_KEY="dev",
            SQLALCHEMY_DATABASE_URI="sqlite:///./test.db",
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    app.register_blueprint(auth_routes)

    return app
