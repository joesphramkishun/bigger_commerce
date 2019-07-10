import hug
import os
import sys
from datetime import datetime
from .api_calls import delete_cart_product, create_user, get_all_users, get_user, add_product, create_cart, \
    add_cart_user, add_billing, add_shipping, update_shipping, test_it, get_cart, create_order, process_payment, \
    payment_token, update_cart_product
import json
import falcon
import os
import logging
import collections
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import string
import random
from app import alembic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .cookie_broker import set_cookie, get_cookie, random_string_generator

#NOTE:: ROUGH DRAFT, MODELS WILL MOST LIKELY NEED TO BE UPDATED AFTER EACH FUNCTION CALL, SAME WITH THE PARAMS WE ARE SENDING
#CART OPERATIONS ONLY
#BILLING ADDRESS IS SAME AS SHIPPING ADDRESS FOR TESTING< CHECK ALEMBIC


logging.basicConfig(level=logging.DEBUG)

ENGINE = create_engine(
    'postgresql+psycopg2://{}:{}@pgdb:5432/bigger_commerce'.format(
        os.getenv("BIGGER_COMMERCE_USER"),
        os.getenv("BIGGER_COMMERCE_PASS")),
    echo=False,
    echo_pool=False)
SESSION = sessionmaker(bind=ENGINE)


#<==========TEST_VARIABLES========================>
'''
pid = 112
cid = '0ea62baf-34e8-4754-a071-7ac2cb81b9b7'

user = {
'uid':2,
'first_name': 'bigg',
"last_name": "tiddies",
"cart_id": '0ea62baf-34e8-4754-a071-7ac2cb81b9b7',
"email": "screwsmalltits@email.com",
"phone": "00000000000",
"address1": "5035 Asbury Parke Dr.",
"city": "Lakeland",
"state_or_province": "Florida",
"state_or_province_code": "FL",
"country_code": "US",
"postal_code": "33805"
}
'''
#<=======TEST API's=========>

# @hug.get('/shipping_practice')#BROKEN ^^ UNDO COMMENT
# def shipping_practice():
#     resp = add_shipping(user)#NOTICE ME SENPAI
#     resp = resp.json()
#     consignment_id = resp['data']['consignments'][0]['id']
#     shipping_options_id = resp['data']['consignments'][0]['available_shipping_options'][0]['id']
#
#     print (consignment_id)
#     print (shipping_options_id)
#
#     dict  = {
#         "consignment_id": consignment_id,
#         "shipping_option" : shipping_options_id,
#         "everything": resp
#     }
#
#     return dict


#register a user and gives login token for that new user
@hug.post('/register')
def test(response, body=None):

    logging.debug("inputting first user ")
    session = SESSION()

    data = body

    password_hash = generate_password_hash(str(data['password']))

    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']

    new_user = alembic.Users(
        email=email,
        password_hash=str(password_hash),
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )
    try:
        logging.debug("attempting to add user")
        session.add(new_user)
        session.commit()
    except:
        logging.error('no go')
        session.rollback()
        message = {"code": "500",
                   "message": "something broke, blame obama"}
        return message

    user = session.query(alembic.Users) \
        .filter(alembic.Users.email == str(data['email'])) \
        .one()

    set_cookie(response, user.uid)

    resp = create_user(user)

    print (resp)

    user.bc_id = resp

    session.add(user)
    session.commit()
    session.close()

    return {"code": "user created",
            "BC_response": resp}
#logs in user and gives login token
@hug.post('/login')
def get_peep(response, body=None):
    session = SESSION()

    data = body

    try:
        user = session.query(alembic.Users) \
            .filter(alembic.Users.email == str(data['email'])) \
            .one()
    except:
        return 'no user found'

    if check_password_hash(user.password_hash, str(data['password'])):
        set_cookie(response, user.uid)
        return 'logged in'
    else:
        return 'that aint it chief'
#checks to see if user is logged in by returning their name
@hug.get('/dashboard')
def dashboard(request,logged_in=None):

    test = request.cookies
    print (test)

    logged_in = get_cookie(request)
    try:
        print (logged_in.first_name)
        name = str(logged_in.first_name)
    except:
        logged_in = None
        name = None

    if logged_in:
        return 'hello {}'.format(name)
    else:
        return 'please login'
#logs out user and takes away login token
@hug.get('/logout')
def call_logout(response):

    response.unset_cookie('cookie')
    return True
#gets info on sepcific user when given a uid
@hug.get('/get_peep')
def get_peep(body=None):

    session = SESSION()
    data = body

    try:
        user  = session.query(alembic.Users) \
            .filter(alembic.Users.email == data['email']) \
            .one()
    except:
        return False

    print (user.bc_id)
    session.close()
    return user.bc_id

#<========================>
#adds item to cart, or if user does not have a cart, creates one for them and adds item
@hug.post('/add_item')#WORKING
def add_item(request, body=None, user=None):

    test = request.cookies
    print(test)
    data = body



    user = get_cookie(request)



    if user:
        # Remember to add cart id to user model
        if user.cart_id:
            add_product(data['pid'], data['quantity'], user.cart_id)

        else:
            cart_id = create_cart(data['quantity'], data['pid'])#initiate cart with nothing, then add

            cart_id = cart_id.json().get('data').get('id')
            print(cart_id)

            add_cart_user(int(user.bc_id), cart_id)#add user id to cart

            new_cart = alembic.Carts(
                uid=user.uid,
                active=True,
                bc_id=cart_id
            )

            user.cart_id = cart_id

            session = SESSION()
            session.add(user)
            session.add(new_cart)
            session.commit()
            session.close()

        return True

    return "Please Login"
#updates cart item
@hug.put('/update_cart_item')#NOTICE ME SENPAI
def update_cart_item(request, body=None):#prob just going to be a quantity change

    user = get_cookie(request)

    data = body

    if user:

        if user.cart_id:
            update_cart_product(user.cart_id, data['pid'], data['quantity'])#update prodcut quantity essentially

        else: return False

        return True

    return "Please Login"
#deletes cart item
@hug.delete('/delete_product')#NOTICE ME SENPAI
def delete_item(request, body=None):
    user = get_cookie(request)

    data = body

    if user:

        if user.cart_id:
            delete_cart_product(data['pid'], user.cart_id)#delete prodcut from the cart

        else: return False

        return True

    return "Please Login"
#returns cart for current user logged in
@hug.get('/get_cart')
def get_user_cart(request):

    user = get_cookie(request)

    if user:

        if user.cart_id != None:
            cart = get_cart(user.cart_id)  #reutrn user's cart

        else:
            return False

        return cart

    return "Please Login"
#deletes whole cart
@hug.delete('/delete_cart')
def delete_user_cart(request):



    user = get_cookie(request)

    if user:

        session = SESSION()
        response = delete_cart_product(user.cart_id)

        user.cart_id = ''

        session.add(user)
        session.commit()
        session.close()


        return response

    return "Please Login"

#takes shipping, billing, and payment info and checks out cart of the current user
@hug.post('/order')
def order(request, body=None):

    data = body
    user = get_cookie(request)

    if user:

        if user.cart_id:

            session = SESSION()

            cart = session.query(alembic.Carts) \
                .filter(alembic.Carts.bc_id == user.cart_id) \
                .one()


            user.address1 = data['address1']
            user.address2 = data['address2']
            user.city = data['city']
            user.state_or_province = data['state_or_province']
            user.state_or_province_code = data['state_or_province_code']
            user.country_code = data['country_code']
            user.postal_code = data['postal_code']
            user.billing_address1 = data['billing_address1']
            user.billing_address2 = data['billing_address2']
            user.billing_city = data['billing_city']
            user.billing_state = data['billing_state']
            user.billing_country_code = data['billing_country_code']
            user.billing_state_code = data['billing_state_code']
            user.billing_postal_code = data['billing_postal_code']
            card_number = data['card_number']
            card_holder_name = data['card_holder_name']
            expiry_month = data['expiry_month']
            expiry_year = data['expiry_year']
            verification_value = data['verification_value']

            billing_response = add_billing(user, cart.bc_id)


            shipping_response = add_shipping(user, cart.bc_id)
            print (shipping_response)
            print (billing_response)

            shipping_response = shipping_response.json()

            print (shipping_response)
            shipping_id = shipping_response['data']['consignments'][0]['id']
            consignment_id = shipping_response['data']['consignments'][0]['available_shipping_options'][0]['id']

            print (consignment_id)
            print(shipping_id)

            cart.shipping_option_id = shipping_id
            cart.consignment_id = consignment_id

            shipping = update_shipping(consignment_id, shipping_id, cart.bc_id)

            order_id = create_order(cart.bc_id)
            order_id = order_id.json()
            order_id = order_id['data']['id']

            cart.order_id = order_id


            payment = payment_token(order_id)
            payment = payment.json()
            payment = payment['data']['id']

            cart.payment_token = payment

            final = process_payment(payment,card_number,card_holder_name, expiry_month,expiry_year,verification_value )

            session.add(user)
            session.add(cart)
            session.commit()
            session.close()


            # order_id = create_order(cart.bc_id)#NOTICE ME SENPAI
            #
            # cart.order_id = order_id
            #
            # print (cart.order_id)

            # shipping_method = add_shipping(user)#can also be added at checkout
            # update_shipping(shipping_method) # // can be implimented in another call if we have multiple shipping options, otherwise use here
            # payment_token(user)#create payment token
            # process_payment(user)#pay token
            #ordeer should be marked 'paid' in BC
            return final
        return "User Has No Cart"
    return "Please Login"