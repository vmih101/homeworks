import sqlite3 as sql


class Database():
    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_jokes(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS jokes ('
                         'id INTEGER PRIMARY KEY,'
                         'joke TEXT UNIQUE,'
                         'favourite TEXT default "n")')

    def parse_jokes(self, jokes):
        self.cur.executemany('INSERT OR IGNORE INTO jokes (joke) VALUES (?)',
                             zip(jokes))
        self.con.commit()

    def select_joke(self):
        self.cur.execute('SELECT id, joke FROM jokes '
                         'WHERE favourite="n"'
                         'ORDER BY random()'
                         'LIMIT 1')
        return self.cur.fetchone()

    def select_fav_joke(self):
        self.cur.execute('SELECT joke FROM jokes '
                         'WHERE favourite="y"'
                         'ORDER BY random()'
                         'LIMIT 1')
        return self.cur.fetchone()

    def upd_fav_joke(self, *joke_id):
        self.cur.execute('UPDATE jokes SET favourite="y" where id=(?)', joke_id)
        self.con.commit()

    def close(self):
        self.con.close()


db1 = Database('jokes.db')
