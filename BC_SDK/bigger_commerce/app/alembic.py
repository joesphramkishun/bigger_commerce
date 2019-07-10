import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Users(BASE):
    __tablename__ = "users"

    uid = sqlalchemy.Column(sqlalchemy.Integer,
                                  primary_key=True,
                                  autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    bc_id = sqlalchemy.Column(sqlalchemy.String)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    current_token = sqlalchemy.Column(sqlalchemy.String)
    cart_id = sqlalchemy.Column(sqlalchemy.String)
    role = sqlalchemy.Column(sqlalchemy.String)
    created_date = sqlalchemy.Column(sqlalchemy.String)
    address1 = sqlalchemy.Column(sqlalchemy.String)
    address2 = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    state_or_province = sqlalchemy.Column(sqlalchemy.String)
    state_or_province_code = sqlalchemy.Column(sqlalchemy.String)
    county_code = sqlalchemy.Column(sqlalchemy.String)
    postal_code = sqlalchemy.Column(sqlalchemy.String)
    billing_address1 = sqlalchemy.Column(sqlalchemy.String)
    billing_address2 = sqlalchemy.Column(sqlalchemy.String)
    billing_city = sqlalchemy.Column(sqlalchemy.String)
    billing_state = sqlalchemy.Column(sqlalchemy.String)
    billing_state_code = sqlalchemy.Column(sqlalchemy.String)
    billing_country_code = sqlalchemy.Column(sqlalchemy.String)
    billing_postal_code = sqlalchemy.Column(sqlalchemy.String)
    gender = sqlalchemy.Column(sqlalchemy.String)

    def as_dict(self):
        dict = {
            "email": self.email,
            "bc_id": self.bc_id,
            "first_name": self.first_name,
            "last_name": self.lat_name,
            "cart_id": self.cart_id,
            "role": self.role,
            "address1": self.address1,
        }
        return dict

class Carts(BASE):
    __tablename__ = "carts"

    id = sqlalchemy.Column(sqlalchemy.Integer,#ACTUAL CART BC_ID
                           primary_key=True,
                           autoincrement=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False) #will put BC UID HERE
    bc_id = sqlalchemy.Column(sqlalchemy.String)
    active = sqlalchemy.Column(sqlalchemy.Boolean)
    created_date = sqlalchemy.Column(sqlalchemy.String)
    order_id = sqlalchemy.Column(sqlalchemy.String)
    shipping_option_id = sqlalchemy.Column(sqlalchemy.String)
    consignment_id = sqlalchemy.Column(sqlalchemy.String)
    payment_token = sqlalchemy.Column(sqlalchemy.String)

    def as_dict(self):
        dict = {
            "uid": self.uid,
            "bc_id": self.bc_id,
            "active": self.active,
        }
        return dict

class Cookies(BASE):
    __tablename__ = "cookies"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    hash_token = sqlalchemy.Column(sqlalchemy.String)
    active = sqlalchemy.Column(sqlalchemy.Boolean)
    created_date = sqlalchemy.Column(sqlalchemy.String)
    ip = sqlalchemy.Column(sqlalchemy.String)




