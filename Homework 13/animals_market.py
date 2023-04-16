import sqlite3 as sql
import requests
from bs4 import BeautifulSoup as bs
from random import randint, choice, randrange
from faker import Faker

class Database():
    def __init__(self):
        self.con = sql.connect('animals.db')
        self.cur = self.con.cursor()

        self.cur.execute('CREATE TABLE IF NOT EXISTS species('
                         'specie_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                         'specie_name TEXT,'
                         'life_expectancy INTEGER,'
                         'UNIQUE (specie_name))')
        self.cur.execute('CREATE TABLE IF NOT EXISTS breeds('
                         'breed_id integer PRIMARY KEY AUTOINCREMENT,'
                         'breed_name TEXT,'
                         'specie_id INTEGER,'
                         'FOREIGN KEY (specie_id) REFERENCES specie (specie_id),'
                         'UNIQUE (breed_name))')
        self.cur.execute('CREATE TABLE IF NOT EXISTS animals('
                         'animal_id integer PRIMARY KEY AUTOINCREMENT,'
                         'animal_name text,'
                         'animal_age integer,'
                         'animal_gender text,'
                         'admission_date text,'
                         'specie_id integer,'
                         'breed_id integer,'
                         'price_byn integer,'
                         'FOREIGN KEY (specie_id) REFERENCES species (specie_id),'
                         'FOREIGN KEY (breed_id) REFERENCES breeds (breed_id),'
                         'UNIQUE(animal_id))')
        self.con.commit()

    def insert_into_species(self, specie_name, life_expectancy):
        self.cur.execute('INSERT OR IGNORE INTO species (specie_name, life_expectancy) VALUES '
                         '(?, ?)', (specie_name, life_expectancy))
        self.con.commit()

    def insert_into_breeds(self, breed_name, specie_id):
        self.cur.execute('INSERT OR IGNORE INTO breeds (breed_name, specie_id) VALUES '
                         '(?, ?)', (breed_name, specie_id))
        self.con.commit()

    def insert_into_animals(self, animal_id, animal_name, animal_age, animal_gender, admission_date, specie_id,
                            breed_id, price_byn):
        self.cur.execute('INSERT OR IGNORE INTO animals (animal_id, animal_name, animal_age, animal_gender,'
                         ' admission_date, specie_id, breed_id, price_byn) VALUES (?,?,?,?,?,?,?,?)',
                         (animal_id, animal_name, animal_age, animal_gender, admission_date, specie_id,
                          breed_id, price_byn))
        self.con.commit()

    def select(self, query, condition=''):
        self.cur.execute(query, condition)
        records = self.cur.fetchall()
        return records



database = Database()

# fill species table
specie_lifespan = {'собака': 15, 'кошка': 14, 'рептилия': 25, 'кролик': 8, 'грызун': 2, 'рыбка': 5, 'амфибия': 15,
                   'попугай': 15}
for i in specie_lifespan:
    database.insert_into_species(i, specie_lifespan.get(i))

#fill breeds table

def parse_breeds(link, animal_id):
    for i in bs(requests.get(url=link).text, 'lxml').find_all('div', 'anketa_name'):
        database.insert_into_breeds(i.find('a').text.lower(), animal_id)

def parse_breeds_fr_titles(link, animal_id):
    for i in bs(requests.get(url=link).text, 'lxml').find_all('div', 'title'):
        database.insert_into_breeds(i.find('a').text.lower(), animal_id)

parse_breeds('https://zvero.ru/rossiya/obyavleniya/sobaki/porody', 1)
parse_breeds('https://zvero.ru/rossiya/obyavleniya/koshki/porody', 2)
parse_breeds_fr_titles('https://zvero.ru/rossiya/obyavleniya/reptilii', 3)
parse_breeds('https://zvero.ru/rossiya/obyavleniya/kroliki/porody', 4)
parse_breeds_fr_titles('https://zvero.ru/rossiya/obyavleniya/gryzuny', 5)
parse_breeds('https://zvero.ru/rossiya/obyavleniya/akvariumnye-rybki/vidy', 6)
parse_breeds_fr_titles('https://zvero.ru/rossiya/obyavleniya/amfibii', 7)
parse_breeds('https://zvero.ru/rossiya/obyavleniya/popugai/vidy', 8)


# fill animals table
fake = Faker()

for animal_id, i in enumerate(range(7), 1):
    animal_name = choice([fake.first_name_male(), fake.first_name_female()])
    specie_id = choice(database.select('SELECT specie_id FROM species'))[0]
    breed_id = choice(database.select('SELECT * FROM breeds where specie_id=(?)', (specie_id,)))[0]
    animal_age = randint(1, int(choice(database.select('SELECT life_expectancy FROM species WHERE specie_id=(?)', (specie_id,)))[0]))
    animal_gender = choice(('male', 'female'))
    admission_date = fake.date_this_year()
    price_byn = randrange(10, 100, 5)
    database.insert_into_animals(animal_id, animal_name, animal_age, animal_gender, admission_date, specie_id, breed_id, price_byn)

print('Animals over 3 years old INNER JOIN\n')
for count, i in enumerate(database.select('SELECT animals.animal_id, animal_name, specie_name, breed_name,'
                                          'animal_age FROM animals '
                                          'JOIN species USING (specie_id) '
                                          'JOIN breeds USING (breed_id)'
                                          'WHERE animal_age > "3"'), 1):
    print(str(count)+'.', i)

print('\n\nAnimals over 2 years old LEFT JOIN\n')
for count, i in enumerate(database.select('SELECT animals.animal_id, animal_name, specie_name, animal_age FROM species '
                         'LEFT JOIN animals USING (specie_id) '
                         'WHERE animal_age > "2"'), 1):
    print(str(count)+'.', i)

print('\n\nAnimals male gender INNER JOIN\n')
for count, i in enumerate(database.select('SELECT * FROM animals '
                         'JOIN breeds USING (breed_id) '
                         'WHERE animals.animal_gender="male"'), 1):
    print(str(count)+'.', i)
