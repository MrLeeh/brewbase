"""
models.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from sqlalchemy import Column, String, Integer, Float, Date, func, Text, \
    ForeignKey
from sqlalchemy.orm import relationship, backref
from app import db


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.now())
    description = Column(Text)
    name = Column(String(255), default='')
    beertype = Column(String(255), default='')
    original_gravity = Column(Float(precision=1))
    alcohol = Column(Float(precision=1))
    bitterness = Column(Integer)
    color = Column(Integer)
    carbonisation = Column(Float(precision=1))

    def __repr__(self):
        return (
            '< Recipe object id={self.id} name={self.name}'
            .format(self=self)
        )

    def copy(self):
        attributes = ['description', 'name', 'beertype', 'original_gravity',
                      'alcohol', 'bitterness', 'color', 'carbonisation']
        recipe = Recipe()
        for attr in attributes:
            setattr(recipe, attr, getattr(self, attr))
        return recipe

    @property
    def ebc(self):
        """
        Calculate color of the recipe by the European Color Convention.

        """
        try:
            return (sum(malt.qty * malt.ebc for malt in self.malts) /
                    sum(malt.qty for malt in self.malts))
        except (TypeError, ZeroDivisionError):
            return None

    @property
    def malt_qty(self):
        """
        Calculate quantity of all used malts.

        """
        try:
            return sum(malt.qty for malt in self.malts)
        except TypeError:
            return None


class RecipeHop(db.Model):
    __tablename__ = 'recipe_hops'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship(
        'Recipe', backref=backref('hops', order_by=id,
                                  cascade='save-update, delete')
    )
    name_ = Column(String(80))
    qty = Column(Float(precision=0))
    alpha_acid = Column(Float(precision=1))
    aroma = Column(Float(precision=1))
    cooking_time = Column(Float())
    comment = Column(Text, default='')

    def copy(self):
        attributes = ['name_', 'qty', 'alpha_acid', 'aroma', 'cooking_time', 'comment']
        new_hop = RecipeHop()
        for attr in attributes:
            setattr(new_hop, attr, getattr(self, attr))
        return new_hop


class RecipeMalt(db.Model):
    __tablename__ = 'recipe_malts'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship(
        'Recipe', backref=backref('malts', order_by=id,
                                  cascade='save-update, delete')
    )
    name_ = Column(String(80))
    qty = Column(Float(precision=1))
    ebc = Column(Float())
    comment = Column(Text, default='')

    def copy(self):
        attributes = ['name_', 'qty', 'ebc', 'comment']
        new_malt = RecipeMalt()
        for attr in attributes:
            setattr(new_malt, attr, getattr(self, attr))
        return new_malt


class RecipeMisc(db.Model):
    __tablename__ = 'recipe_miscs'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship(
        'Recipe', backref=backref('miscs', order_by=id,
                                  cascade='save-update, delete')
    )
    name_ = Column(String(80))
    qty = Column(Float(precision=0))
    comment = Column(Text, default='')

    def copy(self):
        attributes = ['name_', 'qty', 'comment']
        new_misc = RecipeMisc()
        for attr in attributes:
            setattr(new_misc, attr, getattr(self, attr))
        return new_misc


class RecipeMash(db.Model):
    __tablename__ = 'recipe_mash'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship(
        'Recipe', backref=backref('mash', order_by=id,
                                  cascade='save-update, delete')
    )
    name_ = Column(String(80))
    duration = Column(Float(precision=0), default=0)
    temperature = Column(Float(precision=0))
    comment = Column(Text, default='')

    def copy(self):
        attributes = ['name_', 'duration', 'temperature', 'comment']
        new_mash = RecipeMash()
        for attr in attributes:
            setattr(new_mash, attr, getattr(self, attr))
        return new_mash


class Malt(db.Model):
    __tablename__ = 'malt'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    ebc = Column(Float(precision=0))
    comment = Column(Text)


class Hop(db.Model):
    __tablename__ = 'hops'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    alpha_acid = Column(Float(precision=1))
    comment = Column(Text)


class MashTemplate(db.Model):
    __tablename__ = 'mash_templates'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    duration = Column(Float(precision=0))
    temperature = Column(Float(precision=0))
    comment = Column(Text)
