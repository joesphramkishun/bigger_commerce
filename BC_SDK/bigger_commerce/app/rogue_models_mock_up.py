#MODEL MOCK_UP FOR ROGUE SHOPS

#CHECK TO ENSURE ALL THE DATA TYPES LINE UP WITH BIG COMMERCE's

class User(DB.model):

    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.Date, default=datetime.utcnow().date())
    confirmed = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(25), default=UserRole.member)
    current_cart_id = db.Column(db.Integer)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    reset_password_token = db.Column(db.String(128))
    reset_password_time = db.Column(db.DateTime(timezone=True))

    shipping_first = db.Column(db.String(100))
    shipping_last = db.Column(db.String(100))
    shipping_address1 = db.Column(db.String(100))
    shipping_address2 = db.Column(db.String(100))
    shipping_city = db.Column(db.String(100))
    shipping_state = db.Column(db.String(100))
    shipping_zip = db.Column(db.String(100))

    billing_first = db.Column(db.String(100))
    billing_last = db.Column(db.String(100))
    billing_address1 = db.Column(db.String(100))
    billing_address2 = db.Column(db.String(100))
    billing_city = db.Column(db.String(100))
    billing_state = db.Column(db.String(100))
    billing_zip = db.Column(db.String(100))

    provider = db.Column(db.Integer)#(Big Commerrce, Shopify, Magento)
    proivder_id = db.Column(db.Integer)#(Provider ID)
    #add payment_token for remembered credit cards
    client_info_ = db.Column(db.Integer)#TBD


class BC_Cart(DB.model):

    __tablename__ = 'bc_cart'

    cid = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer)
    creation_date = db.Column(db.Date, default=datetime.utcnow().date())
    order_id = db.Column(db.Integer)#104 or something, must be created and put in after final decision
    payment_token = db.Column(db.string(400))#must be made with order_ID pay this and the order is paid w/ BC API
    shipping_option_id = db.Column(db.String(100))#when cart is created with shipping, we must re-update the cart with this shipment method
    consignment_id = db.Column(db.string(50))
    #discounts must be done through Big Commerce API
    #payment_method_id ---- can be added, we prob. will use one payment processor (stripe, braintree, ect.)
    products = db.Column(db.String(1000), default='|')


class Product(DB.model):

    __tablename__ = 'products'

    pid = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.Date, default=datetime.utcnow().date())
    price = db.Column(db.Float)
    title = db.Column(db.String(200))
    name = db.Column(db.String(200))
    description = db.Column(db.string(500))
    url = db.Column(db.String(200), unique=True)
    image_url = db.Column(db.String(200))
    collection_id = db.Column(db.Integer)#needed




#CLIENT MODEL
#TBD

#BC MODEL

    #BC MODEL PARAMS (like shop_name, products, ect.)

    #   def CREATE_CART

    #   def ADD_CART

    #   def ect.

    #   def products


#MAGENTO MODEL

    #Magento MODEL PARAMS (like shop_name, products, ect.)

    #   def CREATE_CART

    #   def ADD_CART

    #   def ect.

    #   def products


#SHOPIFY model

    #SHOPIFY MODEL PARAMS (like shop_name, products, ect.)

    #   def CREATE_CART

    #   def ADD_CART

    #   def ect.

    #   def products
