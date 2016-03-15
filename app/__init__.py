"""
__init__.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models


@app.template_filter('dateformat')
def dateformat(value, format='%d.%m.%Y'):
    return value.strftime(format)
