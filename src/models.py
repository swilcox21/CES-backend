from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    street_address = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(120), unique=False, nullable=True)
    the_state = db.Column(db.String(120), unique=False, nullable=True)
    zip_code = db.Column(db.String(120), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "streetAddress": self.street_address,
            "city": self.city,
            "theState": self.the_state,
            "zipCode": self.zip_code,
            "isActive": self.is_active
            # do not serialize the password, its a security breach
        }

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    unit_price = db.Column(db.Integer, unique=False, nullable=False)
    sub_total = db.Column(db.Integer, unique=False, nullable=False)
    color = db.Column(db.String(120), unique=False, nullable=True)
    size = db.Column(db.String(120), unique=False, nullable=True)
    units = db.Column(db.Integer, unique=False, nullable=False)
    image = db.Column(db.String(5000), unique=False, nullable=True)

    def __repr__(self):
        return '<History %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "unitPrice": self.unit_price,
            "subTotal": self.sub_total,
            "color": self.color,
            "size": self.size,
            "units": self.units,
            "image": self.image,
            # do not serialize the password, its a security breach
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    unit_price = db.Column(db.Integer, unique=False, nullable=False)
    sub_total = db.Column(db.Integer, unique=False, nullable=False)
    color = db.Column(db.String(120), unique=False, nullable=True)
    size = db.Column(db.String(120), unique=False, nullable=True)
    units = db.Column(db.Integer, unique=False, nullable=False)
    image = db.Column(db.String(5000), unique=False, nullable=True)

    def __repr__(self):
        return '<Cart %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "unitPrice": self.unit_price,
            "subTotal": self.sub_total,
            "color": self.color,
            "size": self.size,
            "units": self.units,
            "image": self.image,
            # do not serialize the password, its a security breach
        }

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120), unique=False, nullable=False)
    card = db.Column(db.Integer, unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.String(30), unique=False, nullable=False)

    def __repr__(self):
        return '<Transactions %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "card": self.card,
            "amount": self.amount,
            "status": self.status,
            # do not serialize the password, its a security breach
        }