import sqlite3 as sql
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

LINK = 'https://buklya.com/top-100-knig'


class Database():
    def __init__(self):
        self.con = sql.connect('book_base.db')
        self.cur = self.con.cursor()

    def create_books_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS books'
                         '(id INTEGER PRIMARY KEY,'
                         'name TEXT UNIQUE,'
                         'author TEXT,'
                         'description TEXT)')
        self.con.commit()

    def insert_book(self, name, author, description):
        self.con.execute('INSERT OR IGNORE INTO books (name, author, description)'
                         'VALUES (?, ?, ?)', (name, author, description))
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def select_by_id(self, book_id):
        self.cur.execute("SELECT * FROM books WHERE id=(?)", (book_id,))
        row = self.cur.fetchone()
        return print(row)


database = Database()
database.create_books_table()

ua = UserAgent()
fake_ua = {"user-agent": ua.random}
response = requests.get(url=LINK, headers=fake_ua)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
list_content = soup.find_all('div', 'top_100_book')
for i in list_content:
    name = i.find('span', 'top_100_book_title')
    author = i.find('span', 'top_100_book_author')
    description = i.find('p')
    database.insert_book(name.text, author.text, description.text)

# print all books
for row in database.select_all():
    print(row)

print('\n'*2)

# type book id here
database.select_by_id(1)

