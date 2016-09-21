from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import mapper
from db import metadata, db_sesion


class User(object):
    query = db_session.query_property()