import requests
import sqlite3 as sql


class Database():
    def __init__(self):
        self.con = sql.connect('favourites.db')
        self.cur = self.con.cursor()

    def create_table_favourite_movies(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS favourite_movies'
            '(id INTEGER PRIMARY KEY,'
            'title_ru TEXT UNIQUE,'
            'title_en TEXT,'
            'year INTEGER,'
            'description TEXT,'
            'kp_rating INTEGER)'
        )
        self.con.commit()

    def insert_movie(self, name_ru, name_en, year, descrpition, kp_rating):
        self.cur.execute('INSERT OR IGNORE INTO favourite_movies (title_ru, title_en, year, description, kp_rating) VALUES'
                         ' ( ?, ?, ?, ?, ?)', (name_ru, name_en, year, descrpition, kp_rating))
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return records


database = Database()
database.create_table_favourite_movies()

def parse_movie():
    favorite_list = ['526', '476', '312', '328', '3498', '111543', '279102', '324', '5619', '301']
    LINK = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'
    for i in favorite_list:
        r = requests.get(f"{LINK}{i}", headers={
                                    'X-API-KEY': '090820a4-e8c7-4fcd-b373-4ce6834f2704',
                                    'Content-Type': 'application/json'
                                    }
                     )
        data = r.json()
        database.insert_movie(data['nameRu'], data['nameOriginal'], data['year'], data['shortDescription'], data['ratingKinopoisk'])


parse_movie()

for i in database.select('SELECT * FROM favourite_movies WHERE year > 2005'):
    print(i)