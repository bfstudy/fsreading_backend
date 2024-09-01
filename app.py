from configs.app_config import AppConfig
from extensions.ext_database import db
from extensions import ext_database, ext_migrate
from flask import Flask

def init_extensions(app):
    ext_database.init(app)
    ext_migrate.init(app, db)


def create_app():
    app = Flask(__name__)
    appConfig = AppConfig()
    app.config.from_object(appConfig)
    init_extensions(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7980, debug=True)
