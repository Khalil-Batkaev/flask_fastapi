import threading
import requests

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


def parser_url(url, file_name):
    response = requests.get(url)
    with open(file_name, 'w', encoding='UTF-8') as f:
        f.write(response.text)
    print('Скачал')


threads = []

for i, url in enumerate(URL_LIST):
    t = threading.Thread(target=parser_url, args=(url, f'thread_{i}.txt'))
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(thread.is_alive())

print('OK')
