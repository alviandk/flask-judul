from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
kata_sambung = Table('kata_sambung', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('word', String(length=140)),
)

kolom1 = Table('kolom1', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('word', String(length=140)),
)

kolom2 = Table('kolom2', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('word', String(length=140)),
)

kolom3 = Table('kolom3', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('word', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kata_sambung'].create()
    post_meta.tables['kolom1'].create()
    post_meta.tables['kolom2'].create()
    post_meta.tables['kolom3'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kata_sambung'].drop()
    post_meta.tables['kolom1'].drop()
    post_meta.tables['kolom2'].drop()
    post_meta.tables['kolom3'].drop()
