from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
mash_templates = Table('mash_templates', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('duration', Float(precision=0)),
    Column('temperature', Float(precision=0)),
    Column('comment', Text),
)

recipe_mash = Table('recipe_mash', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name_', String(length=80)),
    Column('duration', Float(precision=0)),
    Column('temperature', Float(precision=0)),
    Column('comment', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['mash_templates'].create()
    post_meta.tables['recipe_mash'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['mash_templates'].drop()
    post_meta.tables['recipe_mash'].drop()
