from extensions.ext_database import db


class Account(db.Model):
    __tablename__ = "accounts"
    __table_args__ = (
        db.UniqueConstraint('username', name='unique_username'),
        db.UniqueConstraint('email', name='unique_email'),
    )
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
