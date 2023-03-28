import json
import sqlite3 as sql


class Database():
    def __init__(self):
        self.con = sql.connect('favourites.db')
        self.cur = self.con.cursor()

    def create_table_desired_devices(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS desired_devices'
            '(id INTEGER PRIMARY KEY,'
            'manufacturer TEXT,'
            'model TEXT UNIQUE,'
            'category TEXT,'
            'price_byn INTEGER)'
        )
        self.con.commit()

    def insert_movie(self, manufacturer, model, category, price_byn):
        self.cur.execute('INSERT OR IGNORE INTO desired_devices (manufacturer, model, category, price_byn) VALUES'
                         ' ( ?, ?, ?, ?)', (manufacturer, model, category, price_byn))
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return records


database = Database()
database.create_table_desired_devices()

def insert_devices():
    with open('devices.json', 'r') as f:
        data = json.load(f)
    for i in data['devices']:
        database.insert_movie(i['manufacturer'], i['model'], i['category'], i['price_byn'])


insert_devices()

for i in database.select('SELECT * FROM desired_devices WHERE price_byn < 1200'):
    print(i)