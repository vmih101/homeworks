from sqlalchemy import create_engine, MetaData, String, Column, Table, Integer, ForeignKey, insert, StaticPool, select, and_, or_
from bs4 import BeautifulSoup as bs
import codecs


engine = create_engine('sqlite:///computer_shop.db', echo=False, poolclass=StaticPool,
                       connect_args={'check_same_thread': False})
engine.connect()


metadata = MetaData()

product = Table('product', metadata,
                Column('maker', String()),
                Column('model', String(), primary_key=True),
                Column('type', String()))

laptop = Table('laptop', metadata,
               Column('code', Integer(), primary_key=True),
               Column('model', String(), ForeignKey('product.model')),
               Column('speed', Integer()),
               Column('ram', Integer()),
               Column('hd', Integer()),
               Column('price', Integer()),
               Column('screen', Integer()))

pc = Table('pc', metadata,
           Column('code', Integer(), primary_key=True),
           Column('model', String(), ForeignKey('product.model')),
           Column('speed', Integer()),
           Column('ram', Integer()),
           Column('hd', Integer()),
           Column('cd', String()),
           Column('price', Integer()))


printer = Table('printer', metadata,
                Column('code', Integer(), primary_key=True),
                Column('model', String(), ForeignKey('product.model')),
                Column('color', String()),
                Column('type', String()),
                Column('price', Integer()))


metadata.create_all(engine)
# metadata.drop_all()

con = engine.connect()


# prepare data to insert in product
def parse_from_html(file_path, list_of_columns):
    html_file = codecs.open(file_path, 'r', 'utf-8').read()
    soup = bs(html_file, 'lxml').find('table', 'st').find_all('tr')
    table_rows = [i.find_all('td') for i in soup if i.find('td')]
    values = [[x.text for x in i] for i in table_rows]
    values_dict = [dict(zip(list_of_columns, i)) for i in values]
    return values_dict


product_values = parse_from_html('html/product.html', ['maker', 'model', 'type'])
pc_values = parse_from_html('html/pc.html', ['code', 'model', 'speed', 'ram', 'hd', 'cd', 'price'])
laptop_values = parse_from_html('html/laptop.html', ['code', 'model', 'speed', 'ram', 'hd', 'price', 'screen'])
printer_values = parse_from_html('html/printer.html', ['code', 'model', 'color', 'type', 'price'])


with engine.connect() as con:
    transaction = con.begin()
    con.execute(insert(product).prefix_with('OR IGNORE'), product_values)
    con.execute(insert(pc).prefix_with('OR IGNORE'), pc_values)
    con.execute(insert(laptop).prefix_with('OR IGNORE'), laptop_values)
    con.execute(insert(printer).prefix_with('OR IGNORE'), printer_values)
    transaction.commit()

query1 = select(pc.c.model, pc.c.speed, pc.c.hd).where(pc.c.price < 500)
query2 = select(laptop).where(laptop.c.price > 1000)
query3 = select(pc).where(and_(or_(pc.c.cd == '12x', pc.c.cd == '24x'), pc.c.price < 600))


with engine.connect() as con:
    print('Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 долларов.'
          ' Вывести: model, speed и hd')
    for i in con.execute(query1):
        print(i)
    print('\nНайдите номер модели, объем памяти и размеры экранов ноутбуков, цена '
          'которых превышает 1000 долларов.')
    for i in con.execute(query2):
        print(i)
    print('\nНайдите номер модели, скорость и размер жесткого диска ПК, имеющих 12х'
          ' или 24х CD и цену менее 600 долларов.')
    for i in con.execute(query3):
        print(i)


