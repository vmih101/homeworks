from sqlalchemy import create_engine, MetaData, StaticPool, Table, Column, Integer, String, ForeignKey


engine = create_engine('sqlite:///books.db', echo=False, poolclass=StaticPool, connect_args={'check_same_thread': False})
metadata = MetaData()

author = Table('author', metadata,
               Column('author_id', Integer(), primary_key=True, autoincrement=True),
               Column('author_name', String(), unique=True),
               Column('about', String()))

genre = Table('genre', metadata,
              Column('genre_id', Integer(), primary_key=True, autoincrement=True),
              Column('genre_name', String(), unique=True))

book = Table('book', metadata,
             Column('book_id', Integer(), primary_key=True, autoincrement=True),
             Column('book_name', String(), unique=True),
             Column('year', Integer()),
             Column('author_id', Integer(), ForeignKey('author.author_id')),
             Column('genre_id', Integer(), ForeignKey('genre.genre_id')),
             Column('description', String()))

metadata.create_all(engine)
print('Database has been created.')