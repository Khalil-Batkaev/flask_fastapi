import threading
from pathlib import Path


def counter(directory):
    with open(directory, 'r', encoding='UTF-8') as f:
        content = f.read().split()
        print(f'Количество слов в {directory}: {len(content)}')


threads = []

for file in Path('.').iterdir():
    if file.is_file:
        threads.append(threading.Thread(target=counter, args=(file, )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('OK')
