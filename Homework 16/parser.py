import aiohttp
import tqdm
import tqdm.asyncio
from bs4 import BeautifulSoup
import asyncio
from utils.database import db1



db1.create_table_jokes()

url_list = [f'http://bashorg.org/page/{i}' for i in range(400)]

async def parse_joke(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            jokes = {i.get_text(separator='\n') for i in soup.find_all('div', 'quote')}
            db1.parse_jokes(jokes)


async def tasks():
    tasks = [parse_joke(url) for url in url_list]
    for f in tqdm.asyncio.tqdm.as_completed(tasks, desc='Async parsing jokes... Await, please',
                                            colour='GREEN', ascii=True):
        await f



asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(tasks())






