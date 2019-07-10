import requests
import json

store_hash = 'gbpc64ceup'

#leaving blank for right now, we can send a uid from our side or whatever // PAYLOADS and URL NEEDS FORMAT, PAYMENT REQUIRES HEADER CHANGE
#ALL GET PARAMS LEFT BLANK (PULLED FORM CONFIG)


#ALL REQUIRMENTS COMMENTED AFTER THE DEFINITION OF A FUNCTION ARE MINIMAL AND MORE {PARAMS} CAN BE ADDED LATER DOWN THE LINE
#WE CAN CREATE ALL PARAMS ON OUR SIDE AND SEND ONE PARAM {ID} AND HAVE THAT FILL IT IN WITH OUR DB

#EVERY API NEEDS THE STORE_ID (shown as gbpc64ceup)
#MANY THINGS CAN BE DONE FROM THE BIG COMMERCE DASHBOARD

#ALL ID's REQUIRED W/ DESCRIPTION enjoii
#--------------------------------------------------------------------------------------------------------------------------------------
#STORE_HASH -- store id (needed for all api calls)

#USER_ID -- BC USER ID (NOT USED MUCH, ASSIGNS PEOPLE TO CARTS/ORDERS)

#PRODUCT_ID -- prodcut ID (used to add to cart)

#CART/CHECKOUT_ID -- CART ID (user_id and product_id needs to be added) ****cart_id && checkout_id are the same***

#ORDER_ID -- ONCE a cart is ready to pay, create an order_ID for said cart (SEE DOCS FOR ALL YOU CAN DO WITH THE ORDER API)

#PAYMENT_TOKEN -- WHEN PAYMENT IS READY< CREATE THIS TOKEN WITH AN ORDER ID, THEN SEND IT TO PROCESS_PAYMENT API w/ PAYMENT INFO

#SHIPPING_OPTION_ID -- given to you when you input the shipping info(it checks to see if it's available), and is added to the CART ID

#PAYMENT_METHOD_ID -- can be seen by get_payment methods (DECIDES WHO WILL PROCESS THE PAYMENT)
#-----------------------------------------------------------------------------------------------------------------------------------------

#please note that in testing, the test card was not working, in live the card processing method
#will test to see if actual card goes through (USE BRAINTREE starting off). Some of these
#API calls will be bundled together when called USING the DB

#LINK TO Big Commerce API DOCS ----  https://developer.bigcommerce.com/api-reference/orders/orders-api/order-shipments/getallordershipments

def test_it(cid):
    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}'.format(store_hash, cid)
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content': 'application/json',
        'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
        'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False)
    print(response.text)
    return response

#<==========USER API's==============================================>

#Creates user for big commerce ((SOMETHING LIKE THIS CAN BE INPUTTED IN TO OUR DB AND PULLED HERE, JUST PASING A ID OR SUMTHIN))
def create_user(user):#First_name, last_name, phone, email

    url = 'https://api.bigcommerce.com/stores/{0}/v2/customers'.format(store_hash)

    payload = {
        "company": "bitmotive",
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone
    }
    print (str(user.email))
    payload = json.dumps(payload)

    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.json().get('id'))#LOOKIE HERE LADDIE
    print (response)

    return response.json().get('id')

#returns all users in big commerce system
def get_all_users():

    url = 'https://api.bigcommerce.com/stores/{0}/v2/customers'.format(store_hash)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#get's info on a specific user
def get_user(uid):#BC user ID

    url = 'https://api.bigcommerce.com/stores/{0}/v2/customers/{1}'.format(store_hash,uid)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)


#<==============================PRODUCT API's==============================================>hug -f

#creates a product
def create_product(pid):#NAME, price, categories, weight, type: (physical/digital)

    url = 'https://api.bigcommerce.com/stores/{0}/v3/catalog/products'.format(store_hash)
    payload = "{\r\n  \"name\": \"Kanye's used tissue\",\r\n  \"price\": \"100.00\",\r\n  \"categories\": [\r\n    23\r\n  ],\r\n  \"weight\": 4,\r\n  \"type\": \"physical\"\r\n}"
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#gets all products
def get_all_products():

    url = 'https://api.bigcommerce.com/stores/{0}/v3/catalog/products'.format(store_hash)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#get specific product info
def get_product(pid):#product_id

    url = 'https://api.bigcommerce.com/stores/{0}/v3/catalog/products/{1}'.format(store_hash,pid)
    payload = {}
    headers = {}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)


#<==================categorie API's=========================================>

#creates category for products to go into (products need a category)
def create_category():#NAME, desc., img url, ect, SEE DOCS

    url = 'https://api.bigcommerce.com/stores/{0}/v3/catalog/categories'.format(store_hash)
    payload = {

    }
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#gets all acategories
def get_all_categories():

    url = 'https://api.bigcommerce.com/stores/{0}/v3/catalog/categories'.format(store_hash)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)


#<============================CART API's=====================================================>

#Creates a Cart, NO USER ATTATCHED (WE CAN MERGE SOME OF THESE API"S INTO ONE CALL)
def create_cart(quantity, pid):#GIVE IT PRODUCT DETAILS AND SO ON, WILL RETURN A CART ID WE WILL NEED TO ASSIGN A USER_ID

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts'.format(store_hash)
    payload = {
        "line_items": [
            {
                "quantity": quantity,
                "product_id": pid
            }
        ]
    }

    payload = json.dumps(payload)

    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    return response

#ADD PRODUCT TO CART
def add_product(pid, quantity, cid):#GIVE PRODUCT DETAILS  and will return a prodcut id SEE DOCS

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}/items'.format(store_hash,cid)
    payload = {
        "line_items": [
            {
                "quantity": quantity,
                "product_id": pid
            }
        ]
    }

    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#UPDATES PRODUCT OF A CART (like quantity)
def update_cart_product(cart, pid, quantity):#CART_ID, PRODUCT ID, and info about product change

    print ('cart: '+ cart)
    print ('pid: '+ str(pid))
    print ('quant: '+ str(quantity))

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}/items/{2}'.format(store_hash, cart, pid)
    payload = {
        "line_item": {
            "quantity": quantity,
            "product_id": pid
        }
    }
    payload = json.dumps(payload)
    headers = {
        'Accept': 'application/json',
        'Content': 'application/json',
        'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
        'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#DELETES PRODUCT FROM CART
def delete_cart_product(pid, cart):#cart_ID, product id

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}/items/{2}'.format(store_hash, cart, pid)
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content': 'application/json',
        'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
        'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('DELETE', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#GETS INFO ABOUT SPECIFIC CART
def get_cart(cid):#CART_ID

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}'.format(store_hash, cid)
    payload = {}
    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)
    return response

#DELETES CART
def delete_cart(cid):#cart id

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}'.format(store_hash, cid)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('DELETE', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response

#ADDS A USER TO A CART /// IMPORTANT
def add_cart_user(user, cart_id):#cart id, user id

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}'.format(store_hash, cart_id)
    payload = {
  "customer_id": user
}
    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return True


#<=====================================CHECKOUT API's=======================================================>

#STARTS CHECKOUT FOR CART (SAME AS CART REALLY)
def get_checkout(cid):#cart id, same as cart

    url = 'https://api.bigcommerce.com/stores/{0}/v3/carts/{1}'.format(store_hash, cid)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#ADDS BILLING ADDRESS FOR CART
def add_billing(user, cid):#cart id, billing  info

    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/billing-address'.format(store_hash, cid)
    payload = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address1": user.billing_address1,
            "address2": user.billing_address2,
            "city": user.billing_city,
            "state_or_province": user.billing_state,
            "state_or_province_code": user.billing_state_code,
            "country_code": user.billing_country_code,
            "postal_code": user.billing_postal_code,
            "phone": user.phone
        }
    payload = json.dumps(payload)

    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response

#UPDATES BILLING ADDRESS FOR CART
def update_billing():#cart id, updated billing info

    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/billing-address/{2}'.format(store_hash, cid, shipping_id)
    payload = {}
    headers = {}
    response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)


#<============================SHIPPING=================================================>

#ADDS SHIPPING ADDRESS TO CART
def add_shipping(user, bc_id):#cart id, shipping address

    cart = get_cart(bc_id)

    print (cart)

    cart = cart.json()

    line_items = cart['data']['line_items']['physical_items']

    for i in range(len(cart['data']['line_items']['physical_items'])):

        product_id = line_items[i]['product_id']

        line_items[i]['item_id'] = product_id


    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/consignments?include=consignments.available_shipping_options'.format(store_hash, bc_id)
    payload = [{
        "shipping_address":{
        "first_name": str(user.first_name),
        "last_name": str(user.last_name),
        "email": str(user.email),
        "address1": str(user.address1),
        "address2": str(user.address2),
        "city": str(user.city),
        "state_or_province": str(user.state_or_province),
        "state_or_province_code": str(user.state_or_province_code),
        "country_code": str(user.country_code),
        "postal_code": str(user.postal_code),
        "phone": str(user.phone)
        },
        "line_items": line_items
    }]

    payload = json.dumps(payload)

    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response

#EDITS SHIPPING FOR CART
def update_shipping(consignment_id, shipping_id, bcid):#cart id, GIVE IT ONE OF THE SHIPPING OPTIONS YOU GOT WHEN YOU PUT IN SHIPPING ADDRESS (SHIPPING_OPTIONS_ID)

    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/consignments/{2}'.format(store_hash, bcid, shipping_id)
    payload = {
        "shipping_option_id": consignment_id
    }
    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response

#<==================================ORDER API's===============================================>

#STARTS ORDER PROCESS FOR A CART (PREVIOUS STEPS REQUIRED TO START THIS PROCESS)
def create_order(cid):#cart_id, gives back order id we will have to use to continue (something like 101)

    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/orders'.format(store_hash, cid)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response

#GET SPECIFIC ORDER INFO
def get_order(oid):#order id

    url = 'https://api.bigcommerce.com/stores/{0}/v2/orders/{1}'.format(store_hash, oid)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#UPDATES AN ORDER
def update_order(oid, updated_info):#order id, update info

    url = 'https://api.bigcommerce.com/stores/{0}/v3/checkouts/{1}/orders'.format(store_hash, cid)
    payload = {}
    headers = {}
    response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#GET ALL ORDERS (status and all)
def get_all_orders():

    url = 'https://api.bigcommerce.com/stores/{0}/v2/orders'.format(store_hash)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)



#<===================================PAYMENT API's==================================================>

#CREATES PAYMENT ACCESS TOKEN FOR AN ORDER (USE NEW TOKEN FOR PAYMENT)
def payment_token(oid):#order id, given back a payment token needed to process payment

    url = 'https://api.bigcommerce.com/stores/{0}/v3/payments/access_tokens'.format(store_hash)
    payload = {
  "order": {
    "id": oid,
    "is_recurring": False
  }
}
    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)
    return response

#GET ALL ACCEPTED PAYMENT METHODS
def accepted_payment_methods():

    url = 'https://api.bigcommerce.com/stores/{0}/v2/payments/methods'.format(store_hash)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#GIVE IT THE PAYMENT TOKEN AND PAYMENT METHOD IN HEADER
def process_payment(token, number,name,  month, year, value):#payment token, payment info  (on completion order status turns to paid or something)

    url = 'https://payments.bigcommerce.com/stores/{0}/payments'.format(store_hash)
    payload = {
        "payment": {
            "instrument": {
                "type": "card",
                "number": number,
                "cardholder_name": name,
                "expiry_month": month,
                "expiry_year": year,
                "verification_value": value
            },
            "payment_method_id": "braintree.card"
        }
    }
    payload = json.dumps(payload)
    headers = {
      'Accept': 'application/vnd.bc.v1+json',
      'Content': 'application/json',
      'Content-Type': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Authorization': 'PAT '+ str(token)
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

    return response



#<====================STORE MANAGER API's=========================================>

#get shipping methods
def shipping_method():

    url = 'https://api.bigcommerce.com/stores/{0}/v2/shipping/zones/{1}/methods'.format(store_hash, ship_method)
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg'
    }
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)

#should be done on admin page, everything needs to be added like accounts and such
def create_shipping_method():#add shipping method, check docs

    url = 'https://api.bigcommerce.com/stores/{0}/v2/shipping/zones/1/methods'.format(store_hash)
    payload = "{\r\n  \"name\": \"Per Order\",\r\n  \"type\": \"perorder\",\r\n  \"settings\": {\r\n    \"rate\": 8\r\n  },\r\n  \"enabled\": true,\r\n  \"handling_fees\": {\r\n    \"fixed_surcharge\": 3\r\n  }\r\n}"
    headers = {
      'Accept': 'application/json',
      'Content': 'application/json',
      'X-Auth-Client': 'yet6twugygv43thqey0lq0yihl8psj',
      'X-Auth-Token': 'lcer5ye0go3p62f2z86150mldfax9pg',
      'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
    print(response.text)
