from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from Users import Users
from sqlalchemy.ext.declarative import declarative_base
db = create_engine('sqlite:///srini.db')
db.echo = True
metadata = MetaData(bind=db)
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)
Base.metadata.create_all(db)
c1 = Car(Name='Oldsmobile', Price=23450)
session.add(c1)
session.commit()
resultset=session.query(Car).filter(Car.Price.in_([23450,3456,4444]))
#session.delete(res)
#session.commit()
for ca in resultset:
    print ca.Name,ca.id