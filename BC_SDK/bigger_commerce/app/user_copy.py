import hug
import click
import os
from datetime import datetime

@hug.get('/')
def user_root():
    # Return Full user object as dict
    return 'Hello from user_root!'

@hug.get('/signup')
def user_signup():
    # Creates a new user an signs them in
    return 'Hello from user_signup!'

@hug.get('/login')
def user_login():
    # Logs user in and makes them current user
    return 'Hello from user_login!'

@hug.get('/logout')
def user_logout():
    # Logs the user out
    return 'Hello from user_logout!'

@hug.get('/reset-password')
def user_reset_password():
    # resets the password for a user
    return 'Hello from user_reset_password!'
