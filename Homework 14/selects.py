from sqlalchemy import select
from database import engine, author, genre, book


query1 = select(author).join(book).limit(10)
query2 = select(book.c.book_id, book.c.book_name, author.c.author_name).join(book, isouter=True).where(book.c.year > 2015)
query3 = select(genre.c.genre_name, book.c.book_name).join(book, isouter=True).where(genre.c.genre_id == 1)

with engine.connect() as con:
    print('\nInner join\n')
    for i in con.execute(query1):
        print(i)
    print('\nOuter join\n')
    for i in con.execute(query2):
        print(i)
    print('\nOuter join\n')
    for i in con.execute(query3):
        print(i)





