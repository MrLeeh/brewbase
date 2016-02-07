"""
forms.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from wtforms import Form, TextField, DateField, DecimalField, IntegerField, \
    TextAreaField
from wtforms.validators import Length, Required


class RecipeForm(Form):
    # date = DateField('Datum:', [Required()], format='%d.%m.%Y')
    name = TextField('Name:', [Length(max=255)])
    description = TextAreaField('Beschreibung:')
    beertype = TextField('Biersorte:', [Length(max=255)])
    original_gravity = DecimalField('Stammwürze:', places=1)
    alcohol = DecimalField('Alkoholgehalt:', places=1)
    bitterness = IntegerField('Bitterkeit:')
    color = IntegerField('Farbe:')
    carbonisation = DecimalField('Karbonisierung:', places=1)
