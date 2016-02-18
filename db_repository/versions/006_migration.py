from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
recipe_malts = Table('recipe_malts', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('recipe_id', INTEGER),
    Column('name', VARCHAR(length=80)),
    Column('qty', FLOAT),
    Column('comment', TEXT),
)

recipe_malts = Table('recipe_malts', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('recipe_id', Integer),
    Column('malt_name', String(length=80)),
    Column('qty', Float(precision=1)),
    Column('comment', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['recipe_malts'].columns['name'].drop()
    post_meta.tables['recipe_malts'].columns['malt_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['recipe_malts'].columns['name'].create()
    post_meta.tables['recipe_malts'].columns['malt_name'].drop()
