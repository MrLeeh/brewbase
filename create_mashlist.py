#!/usr/bin/env python

"""
create_mashlist.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from app.models import MashTemplate
from app import db


templates = [
    MashTemplate(name='Vorlösen', duration=20.0, temperature=20.0),
    MashTemplate(name='Gummirast', duration=20.0, temperature=39.0),
    MashTemplate(name='Weizenrast 1', duration=15.0, temperature=45.0),
    MashTemplate(name='Weizenrast 2', duration=15.0, temperature=48.0),
    MashTemplate(name='Eiweißrast', duration=10.0, temperature=52.0),
    MashTemplate(name='Maltoserast', duration=45.0, temperature=63.0),
    MashTemplate(name='Verzuckerung', duration=30.0, temperature=72.0),
    MashTemplate(name='Abmaischen', duration=20.0, temperature=78.0)

]

MashTemplate.query.delete()
db.session.add_all(templates)
db.session.commit()
