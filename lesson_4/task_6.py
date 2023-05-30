import asyncio
from pathlib import Path


async def counter(directory):
    with open(directory, 'r', encoding='UTF-8') as f:
        content = f.read().split()
        print(f'Количество слов в {directory}: {len(content)}')


if __name__ == '__main__':
    tasks = []

    for file in Path('.').iterdir():
        if file.is_file:
            task = asyncio.ensure_future(counter(file))
            tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print('OK')