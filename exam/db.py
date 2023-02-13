import sqlite3 as sql
import requests
import random
 
class Database():
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()
 
    def create_table_clients(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phone INTEGER)')
        self.con.commit()

    def insert_to_clients(self, new_data):
        self.cur.executemany("INSERT INTO clients (name, age, phone) VALUES (?, ?, ?)", new_data)
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return print(records)

    def close(self):
        self.con.close()

    def write_to_txt(self, query):
        with open("clients.txt", 'w') as f:
            for row in self.cur.execute(f"{query}"):
                x = [str(a) for a in row]
                f.write(", ".join(x) + '\n')
 
def input_clients():
    new_data = []
    while True:
        new_client_str = input('Input new client data in format like (Vlad 29 375298073264) or input "stop":').split()
        if new_client_str[0] == 'stop':
            break
        new_data.append(new_client_str)
    return new_data


database = Database("clients.db")
database.create_table_clients()
new_clients = input_clients()
database.insert_to_clients(new_clients)
database.write_to_txt('SELECT * FROM clients ORDER BY age DESC')





