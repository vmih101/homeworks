from sqlalchemy import insert, select
from bs4 import BeautifulSoup, element
import requests
import asyncio
import aiohttp
import tqdm.asyncio
from aiohttp_retry import RetryClient, JitterRetry
from fake_useragent import UserAgent
from database import engine, author, genre, book


def get_soup(url):
    response = requests.get(url=url)
    return BeautifulSoup(response.text, 'lxml').find_all('div', class_='book-cardLong')


def get_authors_urls(soup):
    lst = {f'{domain}{i.find("a", class_="book-cardLong-author")["href"]}' for i in soup}
    return lst


def get_books_urls(soup):
    lst = {f'{domain}{i.find("a")["href"]}' for i in soup}
    return lst


async def authors_soups_parser(url):
    async with aiohttp.ClientSession(headers={'user-agent': ua.random}) as session:
        retry_options = JitterRetry()
        retry_client = RetryClient(client_session=session, retry_options=retry_options)
        async with retry_client.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            authors_soups.append(soup)


async def books_soups_parser(url):
    async with aiohttp.ClientSession(headers={'user-agent': ua.random}) as session:
        retry_options = JitterRetry(attempts=10)
        retry_client = RetryClient(client_session=session, retry_options=retry_options)
        async with retry_client.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            books_soups.append(soup)


async def run_tasks():
    authors = [authors_soups_parser(url) for url in get_authors_urls(soup)]
    for f in tqdm.asyncio.tqdm.as_completed(authors, desc='Async parsing authors pages... Await, please',
                                            colour='GREEN', ascii=True):
        await f
    books = [books_soups_parser(url) for url in get_books_urls(soup)]
    for f in tqdm.asyncio.tqdm.as_completed(books, desc='Async parsing books pages... Await, please',
                                            colour='GREEN', ascii=True):
        await f

url = 'https://libs.ru/best-100-foreign/'
domain = 'https://libs.ru'
ua = UserAgent()
authors_soups = []
books_soups = []
genres_values = []
authors_values = []
books_values = []

soup = get_soup(url)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(run_tasks())


for i in authors_soups:
    if isinstance(i.find('div', itemprop='description'), element.Tag):
        authors_values.append({'author_name': i.find('h1').text, 'about': ' '.join(
            [x.text for x in i.find('div', itemprop='description').find_all('p')])})
    else:
        authors_values.append({'author_name': i.find('h1').text, 'about': ''})

for i in books_soups:
    genres_values.append({'genre_name': i.find('div', 'genre').find_all('a')[-1].text})

with engine.connect() as con:
    transaction = con.begin()
    con.execute(insert(author).prefix_with('OR IGNORE'), authors_values)
    con.execute(insert(genre).prefix_with('OR IGNORE'), genres_values)
    transaction.commit()

for i in books_soups:
    book_columns = ['book_name', 'year', 'author_id', 'genre_id', 'description']
    book_name = i.find('h1').text
    if len(i.find('div', 'book-param').find_all('a')) == 2:
        year = i.find('div', 'book-param').find_all('a')[1].text.split()[0]
    else:
        year = ''
    author_id = engine.connect().execute(select(author.c.author_id).where(author.c.author_name == i.find('a', 'book-author').text)).fetchone()[0]
    genre_id = engine.connect().execute(select(genre.c.genre_id).where(genre.c.genre_name == i.find('div', 'genre').find_all('a')[-1].text)).fetchone()[0]
    description = i.find('div', itemprop='description').find('p').text
    books_values.append(dict(zip(book_columns, [book_name, year, author_id, genre_id, description])))

with engine.connect() as con:
    transaction = con.begin()
    con.execute(insert(book).prefix_with('OR IGNORE'), books_values)
    transaction.commit()

print('Data have been parsed and inserted')