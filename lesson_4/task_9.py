
import requests
import aiohttp
import asyncio
from multiprocessing import Process
from threading import Thread
import time
from pathlib import Path
import sys


"""
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение 
должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе. Например 
URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg  Программа должна использовать 
многопоточный, многопроцессорный и асинхронный подходы. Программа должна иметь возможность задавать список 
URL-адресов через аргументы командной строки. Программа должна выводить в консоль информацию о времени скачивания 
каждого изображения и общем времени выполнения программы.
"""

URL = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Phalacrocorax_carbo%2C_Egretta_garzetta_and_Mareca_strepera_in_Taudha_Lake.jpg/2560px-Phalacrocorax_carbo%2C_Egretta_garzetta_and_Mareca_strepera_in_Taudha_Lake.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Ethiopia_Banna_tribe_kids.jpg/2560px-Ethiopia_Banna_tribe_kids.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pillars_of_Creation_%28NIRCam_Image%29.jpg/1024px-Pillars_of_Creation_%28NIRCam_Image%29.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Church_of_light.jpg/2560px-Church_of_light.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Siebenpunkt-Marienk%C3%A4fer_%28Coccinella_septempunctata%29_auf_Bl%C3%BCte_im_FFH-Gebiet_%22Viernheimer_Waldheide_und_angrenzende_Fl%C3%A4chen%22.jpg/2560px-Siebenpunkt-Marienk%C3%A4fer_%28Coccinella_septempunctata%29_auf_Bl%C3%BCte_im_FFH-Gebiet_%22Viernheimer_Waldheide_und_angrenzende_Fl%C3%A4chen%22.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/A_foggy_winter_morning.jpg/2560px-A_foggy_winter_morning.jpg'
]


def get_img(url, name):
    start = time.time()
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(Path('img', name, file_name), 'wb') as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time() - start:.2f}seconds")


async def async_get_img(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            _response = await response.read()
            file_name = url.split('/')[-1]
            with open(Path('img', 'async', file_name), 'wb') as f:
                f.write(_response)
                print(f"Downloaded {url} in {time.time() - start:.2f}seconds")


if __name__ == '__main__':
    threads = []
    print(f'Запуск Многопоточность')
    start_time = time.time()

    for link in URL:
        t = Thread(target=get_img, args=(link, 'thread'))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    print(f'Завершение Многопоточность за {time.time() - start_time:.2f} секунд')

    processes = []
    print(f'Запуск Многопроцессорность')
    start_time = time.time()

    for link in URL:
        p = Process(target=get_img, args=(link, 'process'))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print(f'Завершение Многопроцессорность за {time.time() - start_time:.2f} секунд')

    print(f'Запуск Асинхрон')
    start_time = time.time()
    tasks = []
    for link in URL:
        task = asyncio.ensure_future(async_get_img(link))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'Завершение Асинхрон за {time.time() - start_time:.2f} секунд')
