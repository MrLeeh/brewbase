"""
forms.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from .models import RecipeMalt, RecipeHop, RecipeMisc
from flask.ext.wtf import Form
from wtforms import FieldList, ValidationError
from wtforms import Form as NoCsrfForm
from wtforms.fields import TextField, DecimalField, IntegerField, \
    TextAreaField, FormField
from wtforms.validators import Length, Optional, Required


def empty_or_decimal(form, field):
    if field.data == '':
        return True
    try:
        float(field.data)
    except (ValueError, TypeError):
        raise ValidationError('Not a valid decimal value')
    return True


class MaltForm(NoCsrfForm):
    name_ = TextField('Name:', [Length(max=80), Required()])
    qty = DecimalField('Menge (kg):')
    ebc = DecimalField('Farbe (EBC)', places=0)
    comment = TextAreaField('Bemerkungen:')


class HopForm(NoCsrfForm):
    name_ = TextField('Name:', [Length(max=80)])
    qty = DecimalField('Menge:', places=0)
    alpha_acid = DecimalField('Alpha-Säure:', places=0)
    cooking_time = DecimalField('Kochzeit:', places=0)
    comment = TextAreaField('Bemerkungen:')


class MiscForm(NoCsrfForm):
    name_ = TextField('Name:', [Length(max=80)])
    qty = DecimalField('Menge:', places=0)
    comment = TextAreaField('Bemerkungen:')


class RecipeForm(Form):
    # date = DateField('Datum:', [Required()], format='%d.%m.%Y')
    name = TextField('Name:', [Length(max=255)])
    description = TextAreaField('Beschreibung:')
    beertype = TextField('Biersorte:', [Length(max=255)])
    original_gravity = DecimalField('Stammwürze:', places=1)
    alcohol = DecimalField('Alkoholgehalt:', places=1, validators=[Optional()])
    bitterness = IntegerField('Bitterkeit:')
    color = IntegerField('Farbe:')
    carbonisation = DecimalField('Karbonisierung:', places=1)
    malts = FieldList(FormField(MaltForm, default=lambda: RecipeMalt()))
    hops = FieldList(FormField(HopForm, default=lambda: RecipeHop()))
    miscs = FieldList(FormField(MiscForm, default=lambda: RecipeMisc()))
