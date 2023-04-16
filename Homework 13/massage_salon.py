import sqlite3 as sql
import random
from faker import Faker

class Database():
    def __init__(self):
        self.con = sql.connect('massage_salon.db')
        self.cur = self.con.cursor()

    def create_table_clients(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS clients('
                         'client_id INTEGER PRIMARY KEY UNIQUE,'
                         'first_name TEXT,'
                         'last_name TEXT,'
                         'number TEXT,'
                         'UNIQUE(first_name, last_name, number)'
                         ')')
        self.con.commit()

    def create_table_services(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS services('
                         'service_id INTEGER PRIMARY KEY,'
                         'service_name TEXT UNIQUE,'
                         'price_usd INTEGER'
                         ')')
        self.con.commit()

    def create_table_orders(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS orders('
                         'order_id INTEGER PRIMARY KEY,'
                         'client_id INTEGER,'
                         'service_id INTEGER,'
                         'date TEXT,'
                         'time TEXT,'
                         'FOREIGN KEY (client_id) REFERENCES clients(client_id),'
                         'FOREIGN KEY (service_id) REFERENCES services(service_id),'
                         'UNIQUE(date, time)'
                         ')')

    def insert_into_clients(self, client_id, first_name, last_name, number):
        self.cur.execute('INSERT OR IGNORE INTO clients (client_id, first_name, last_name, number) VALUES (?, ?, ?, ?)',
                         (client_id, first_name, last_name, number))
        self.con.commit()

    def insert_into_services(self, service_name, price_usd):
        self.cur.execute('INSERT OR IGNORE INTO services (service_name, price_usd) VALUES (?, ?)',
                         (service_name, price_usd))
        self.con.commit()

    def insert_into_orders(self, order_id, client_id, service_id, date, time):
        self.cur.execute('INSERT OR IGNORE INTO orders (order_id, client_id, service_id, date, time) VALUES (?, ?, ?, ?, ?)',
                         (order_id, client_id, service_id, date, time))
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'{query}')
        result = self.cur.fetchall()
        return result


database = Database()

database.create_table_services()
database.create_table_clients()
database.create_table_orders()

services_list = ['общий', 'спины', 'поясничного отдела', 'грудного отдела', 'шеи и шейно-воротниковой зоны', 'головы',
                 'рук', 'ног', 'антицеллюлитный', 'оздоровительный', 'лимфодренажный', 'тайский', 'стоун-терапия',
                 'медовый']

# fill services table
for i in services_list:
    database.insert_into_services(i, random.randrange(50, 150, 5))

# fill clients table
fake = Faker('ru_RU')
for id in range(1, 101):
    name = random.choice([[fake.first_name_male(), fake.last_name_male()],
                         [fake.first_name_female(), fake.last_name_female()]])
    database.insert_into_clients(id, name[0], name[1], fake.phone_number())

# fill orders table
for id in range(1, 51):
    database.insert_into_orders(id, random.randint(1, 100), random.randint(1, 14),
                                fake.date_this_month(before_today=False, after_today=True),
                                f'{random.randint(9, 20)}:{random.choice(("00", "30"))}')

for i in database.select('SELECT orders.order_id, clients.first_name, clients.last_name, services.service_name, orders.date,'
                         'orders.time FROM orders '
                         'JOIN clients ON (orders.client_id=clients.client_id) '
                         'JOIN services ON (orders.service_id=services.service_id)'):
    print(i)


