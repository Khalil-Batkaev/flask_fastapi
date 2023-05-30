import asyncio
import aiohttp

URL_LIST = [
    'https://gb.ru/',
    'https://google.com',
    'https://yandex.ru',
    'https://python.org',
    'https://mail.ru',
    'https://rambler.ru',
    'https://vk.com',
    'https://yahoo.com',
]


async def parser_url(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_name, 'w', encoding='UTF-8') as f:
                _response = await response.text()
                f.write(_response)


if __name__ == '__main__':
    tasks = []
    for i, url in enumerate(URL_LIST):
        task = asyncio.ensure_future(parser_url(url, f'async_{i}.html'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
