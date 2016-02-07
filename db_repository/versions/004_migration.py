from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
recipes = Table('recipes', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('description', String),
    Column('name', String(length=255), default=ColumnDefault('')),
    Column('beertype', String(length=255), default=ColumnDefault('')),
    Column('original_gravity', Float(precision=1)),
    Column('alcohol', Float(precision=1)),
    Column('bitterness', Integer),
    Column('color', Integer),
    Column('carbonisation', Float(precision=1)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recipes'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recipes'].columns['description'].drop()
