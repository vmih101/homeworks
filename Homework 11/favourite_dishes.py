import json
import sqlite3 as sql


class Database():
    def __init__(self):
        self.con = sql.connect('favourites.db')
        self.cur = self.con.cursor()

    def create_table_dishes_list(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS dishes_list(dish_id INTEGER PRIMARY KEY, title TEXT, receipt TEXT)')
        self.con.commit()

    def create_table_ingredients_list(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS ingredients_list(ingredient_id INTEGER PRIMARY KEY, title TEXT UNIQUE)')
        self.con.commit()

    def create_table_measurement(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS measurement(unit_id INTEGER PRIMARY KEY, title TEXT UNIQUE)')
        self.con.commit()

    def create_table_calorie(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS calorie(dish_id INTEGER, proteins INTEGER, fats INTEGER, carbohydrates INTEGER, calorie INTEGER, FOREIGN KEY (dish_id) REFERENCES dishes_list(dish_id))')
        self.con.commit()

    def create_table_grocery_list(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS grocery_list(dish_id INTEGER, ingredient_id INTEGER, value INTEGER,'
                         ' unit_id INTEGER, FOREIGN KEY (dish_id) REFERENCES dishes_list(dish_id), FOREIGN KEY (ingredient_id) REFERENCES ingredients_list(ingredient_id), FOREIGN KEY (unit_id) REFERENCES measurement(unit_id))')
        self.con.commit()

    def create_view_full_receipt(self):
        self.cur.execute('CREATE VIEW IF NOT EXISTS full_receipt AS '
                         'SELECT DISTINCT d.dish_id AS ID, d.title AS "Блюдо", d.receipt AS "Рецепт", i.title AS '
                         '"Ингредиент", g.value AS "Количество", m.title AS  "Единица измерения", c.proteins AS "Белки", c.fats AS '
                         '"Жиры", c.carbohydrates AS "Углеводы", c.calorie "Калорийность" '
                         'FROM dishes_list AS d '
                         'JOIN calorie AS c ON d.dish_id = c.dish_id '
                         'JOIN grocery_list AS g ON d.dish_id = g.dish_id '
                         'JOIN measurement AS m ON g.unit_id = m.unit_id '
                         'JOIN ingredients_list AS i ON g.ingredient_id = i.ingredient_id;')
        self.con.commit()

    def json_receipt(self):
        with open('receipts.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def refresh_products_measurements(self):
        data = self.json_receipt()
        ingredients = []
        for i in data['dishes']:
            keys_list = []
            keys_list.append(iter(i['ingredients'].keys()))
            for i in keys_list[0]:
                ingredients.append(i)
        measurements = []
        for i in data['dishes']:
            values_list = []
            values_list.append(iter(i['ingredients'].values()))
            for i in values_list[0]:
                measurements.append(i[1])
        for i in ingredients:
            self.cur.execute('INSERT OR IGNORE INTO ingredients_list (title) VALUES (?)', (i,))
        for i in measurements:
            self.cur.execute('INSERT OR IGNORE INTO measurement (title) VALUES (?)', (i,))
        self.con.commit()

    def insert_receipt(self):
        data = self.json_receipt()
        print(data['dishes'][0]['calories'])
        for i in data['dishes']:
            self.con.execute('INSERT OR IGNORE INTO dishes_list VALUES (?, ?, ?)', (i['ID'], i['name'], i['receipt']))
            self.con.execute('INSERT OR IGNORE INTO calorie VALUES (?, ?, ?, ?, ?)',
                             (i['ID'], i['calories'].get('proteins'), i['calories'].get('proteins'),
                              i['calories'].get('fats'), i['calories'].get('carbohydrates')))
            for x in list(i['ingredients']):
                self.con.execute('INSERT OR IGNORE INTO grocery_list VALUES (?, (SELECT ingredient_id FROM '
                                 'ingredients_list WHERE title = ?), ?, (SELECT unit_id FROM measurement WHERE title '
                                 '= ?))', (i['ID'], x, i['ingredients'].get(x)[0], i['ingredients'].get(x)[1]))
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return print(records)


def json_receipt():
    with open('receipts.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    return data


def refresh_products_measurements():
    data = json_receipt()
    ingredients = []
    for i in data['dishes']:
        keys_list = []
        keys_list.append(iter(i['ingredients'].keys()))
        for i in keys_list[0]:
            ingredients.append(i)
    return ingredients


database = Database()
database.create_table_dishes_list()
database.create_table_ingredients_list()
database.create_table_measurement()
database.create_table_calorie()
database.create_table_grocery_list()
database.refresh_products_measurements()
database.insert_receipt()
database.create_view_full_receipt()
database.select('SELECT * FROM full_receipt WHERE ID = 1')


