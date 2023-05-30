import multiprocessing
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


if __name__ == '__main__':
    processes = []

    for i, url in enumerate(URL_LIST):
        t = multiprocessing.Process(target=parser_url, args=(url, f'process_{i}.txt'))
        processes.append(t)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print('OK')
