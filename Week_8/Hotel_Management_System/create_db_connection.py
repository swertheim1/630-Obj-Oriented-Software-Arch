"""
Create database and database connection

"""

import os
from sqlalchemy import create_engine


def local_connection():

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'hotel_management.db')

    # create engine object
    engine = create_engine(connection_string, echo=False)
    print('<<<< CREATING ENGINE >>>>')
    # establish a connection to the database
    return engine


