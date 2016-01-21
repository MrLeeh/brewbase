"""
__init__.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import Flask

app = Flask(__name__)
from app import views
