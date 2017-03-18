from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, MetaData)

db = create_engine('sqlite:///srini.db')

meta = MetaData()
meta.reflect(bind=db)

for table in meta.tables:
    print table