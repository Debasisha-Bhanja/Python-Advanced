class Book(Base):  #<-------------------------
    __tablename__  = "books"    #matches the name of the actual database table
    id             = Column(Integer,Sequence('book_seq'),primary_key=True) # plays nice with all major database engines
    name           = Column(String(50))                                    # string column need lengths
    author_id      = Column(Integer,ForeignKey('authors.id'))              # assumes there is a table in the database called 'authors' that has an 'id' column
    price          = Column(Float)
    date_added     = Column(DateTime, default=datetime.datetime.now)       # defaults can be specified as functions
    promote        = Column(Boolean,default=False)                         #     or as values