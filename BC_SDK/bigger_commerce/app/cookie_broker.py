import sqlalchemy.orm
import logging
import os
import string
import random
from app import alembic


logging.basicConfig(level=logging.DEBUG)

ENGINE = sqlalchemy.create_engine(
    'postgresql+psycopg2://{}:{}@pgdb:5432/bigger_commerce'.format(
        os.getenv("BIGGER_COMMERCE_USER"),
        os.getenv("BIGGER_COMMERCE_PASS")),
    echo=False,
    echo_pool=False)
SESSION = sqlalchemy.orm.sessionmaker(bind=ENGINE)


def set_cookie(response, uid):

    session=SESSION()
    new_token = random_string_generator()
    #call user where uid == uid
    user = session.query(alembic.Users)\
        .filter(alembic.Users.uid == uid)\
        .one()

    user.current_token = str(new_token)
    try:
        update_old_token = session.query(alembic.Cookies)\
            .filter(alembic.Cookies.uid == uid, alembic.Cookies.active == True)\
            .one()
        update_old_token.active = False
        session.add(update_old_token)
        session.commit()
    except: pass

    token_params = alembic.Cookies(
        uid = uid,
        hash_token = str(new_token),
        active = True
    )


    logging.debug('attempting to update DB with token info.')
    session.add(token_params)
    session.add(user)
    session.commit()

    response.set_cookie('cookie', new_token)

    session.close()

    return 'success'

def get_cookie(request):

    session = SESSION()

    token = request.cookies
    print (token)
    logging.debug(token)

    try:
        cookie = token['cookie']
    except:
        logging.debug('no cookies =(')
        return None


    ticket = session.query(alembic.Cookies)\
        .filter(alembic.Cookies.hash_token == cookie)\
        .one()

    if (ticket.active == True):

        user = session.query(alembic.Users)\
            .filter(alembic.Users.uid == ticket.uid)\
            .one()

        first_name = user.first_name
        print (first_name)

        session.close()

        return user
    else:
        return False



def random_string_generator(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))