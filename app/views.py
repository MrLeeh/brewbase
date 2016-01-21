"""
views.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
