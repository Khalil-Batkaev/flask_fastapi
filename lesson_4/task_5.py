import multiprocessing
from pathlib import Path


def counter(directory):
    with open(directory, 'r', encoding='UTF-8') as f:
        content = f.read().split()
        print(f'Количество слов в {directory}: {len(content)}')


if __name__ == '__main__':
    processes = []

    for file in Path('.').iterdir():
        if file.is_file:
            processes.append(multiprocessing.Process(target=counter, args=(file, )))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print('OK')
