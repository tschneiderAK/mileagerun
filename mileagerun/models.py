from mileagerun import db

class User(db.Model):
    __tablename__ = "users"
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

earning = db.Table('earning_by_miles', db.metadata, autoload=True, autoload_with=db.engine)