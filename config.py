"""
config.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
import os


SECRET_KEY = 'this is my very secret key'
WTF_CSRF_ENABLED = True

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
