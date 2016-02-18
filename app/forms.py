"""
forms.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from .models import RecipeMalt, RecipeHop
from flask.ext.wtf import Form
from wtforms import FieldList
from wtforms import Form as NoCsrfForm
from wtforms.fields import TextField, DecimalField, IntegerField, \
    TextAreaField, FormField
from wtforms.validators import Length, Required


class MaltForm(NoCsrfForm):
    name_ = TextField('Name:', [Length(max=80)])
    qty = DecimalField('Menge (kg):')
    comment = TextAreaField('Bemerkungen:')


class HopForm(NoCsrfForm):
    name_ = TextField('Name:', [Length(max=80)])
    qty = IntegerField('Menge:')
    comment = TextAreaField('Bemerkungen:')


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
    malts = FieldList(FormField(MaltForm, default=lambda: RecipeMalt()))
    hops = FieldList(FormField(HopForm, default=lambda: RecipeHop()))
