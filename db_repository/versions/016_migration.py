from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
recipe_hops = Table('recipe_hops', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('recipe_id', Integer),
    Column('name_', String(length=80)),
    Column('qty', Float(precision=0)),
    Column('alpha_acid', Float(precision=1)),
    Column('aroma', Float(precision=1)),
    Column('cooking_time', Float),
    Column('comment', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recipe_hops'].columns['alpha_acid'].create()
    post_meta.tables['recipe_hops'].columns['aroma'].create()
    post_meta.tables['recipe_hops'].columns['cooking_time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recipe_hops'].columns['alpha_acid'].drop()
    post_meta.tables['recipe_hops'].columns['aroma'].drop()
    post_meta.tables['recipe_hops'].columns['cooking_time'].drop()
