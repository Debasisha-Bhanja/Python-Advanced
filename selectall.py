from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select
from Users import Users

eng = create_engine('sqlite:///srini.db')

with eng.connect() as con:
    meta = MetaData(eng)
    cars = Table('Users', meta, autoload=True)

    stm = select([Users])
    rs = con.execute(stm)

    print rs.fetchall()