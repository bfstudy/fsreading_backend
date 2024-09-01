from . import apollo_client
from urllib.parse import quote_plus


class DatabaseConfig(object):
    DB_HOST = apollo_client.get_value("db-host")
    DB_PORT = apollo_client.get_value("db-port")
    DB_URI_SCHEME = apollo_client.get_value("db-uri-scheme")
    DB_USERNAME = apollo_client.get_value("db-username")
    DB_PASSWORD = apollo_client.get_value("db-password")
    DB_DATABASE = apollo_client.get_value("db-database")
    DB_CHARSET = apollo_client.get_value("db-charset")
    DB_EXTRAS = apollo_client.get_value("db-extras")

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db_extras = (
            f"{self.DB_EXTRAS}&charset={self.DB_CHARSET}"
            if self.DB_CHARSET
            else self.DB_EXTRAS
        ).strip("&")
        db_extras = f"?{db_extras}" if db_extras else ""
        return (
            f"{self.DB_URI_SCHEME}://"
            f"{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"
            f"{db_extras}"
        )
