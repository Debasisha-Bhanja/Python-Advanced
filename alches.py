from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.sql import select

engine = create_engine('sqlite:///tutorial.db',
                       echo=True)

metadata = MetaData(bind=engine)

users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('age', Integer),
                    Column('password', String),
                    )

addresses_table = Table('addresses', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('email_address', String, nullable=False)
                        )

# create tables in database
metadata.create_all()
ins = users_table.insert()
# add values to the Insert object
new_user = ins.values(name="Joe", age=20, password="pass")

# create a database connection
conn = engine.connect()
# add user to database by executing SQL
conn.execute(new_user)
s = select([users_table])
result = s.execute()

for row in result:
    print (row)