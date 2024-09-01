from flask_migrate import Migrate

migrate = Migrate()


def init(app, db):
    migrate.init_app(app, db)
