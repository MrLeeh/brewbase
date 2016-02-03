"""
models.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from sqlalchemy import Column, String, Integer, Float, Date, func
from app import db


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.now())
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
