import asyncio
import multiprocessing
from multiprocessing import Process
from random import randint
from threading import Thread
import time

"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.  Пример массива: 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] Массив должен быть заполнен случайными целыми числами от 1 до 100. При 
решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.  В каждом решении нужно 
вывести время выполнения вычислений.
"""


def thread_sum_array(array: list):
    global thread_result
    thread_result += sum(array)


def thread_calculations(array: list, func=thread_sum_array):
    t = Thread(target=func, args=(array, ))
    t.start()
    return t


def process_sum_array(array: list, res):
    with res.get_lock():
        res.value += sum(array)


def process_calculations(array: list, res, func=process_sum_array):
    p = Process(target=func, args=(array, res))
    p.start()
    return p


async def async_sum_array(array: list) -> int:
    async_result = sum(array)
    return async_result


async def main(array):
    tasks = []
    j = 0

    for i in range(STEP, LIMIT + STEP, STEP):
        tasks.append(async_sum_array(array[j:i]))
        j = i

    result = await asyncio.gather(*tasks)
    return sum(result)


if __name__ == '__main__':
    MIN = 1
    MAX = 100 + 1
    LIMIT = 10_000_000
    QTY = 5
    STEP = LIMIT // QTY
    OPERATIONS = {
        'Многопоточность': thread_calculations,
        'Многопроцессорность': process_calculations,
    }

    thread_result = 0
    process_result = multiprocessing.Value('i', 0)
    numbers = [randint(MIN, MAX) for _ in range(LIMIT)]
    print(f'Контрольная сумма: {sum(numbers):_}')

    for operation, func in OPERATIONS.items():
        start_time = time.time()
        j = 0
        operations_list = []

        print(f'Старт операции: {operation}')

        for i in range(STEP, LIMIT + STEP, STEP):
            _operation = func(numbers[j:i]) if operation == "Многопоточность" else func(numbers[j:i], process_result)
            operations_list.append(_operation)
            j = i

        for oper in operations_list:
            oper.join()

        print(f'Завершение операции: {operation}, время выполнения: {time.time() - start_time:.2f} секунд, '
              f'сумма = {thread_result if operation == "Многопоточность" else process_result.value:_}')

    print(f'Старт операции: Асинхронно')
    start_time = time.time()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(numbers))
    print(f'Завершение операции: Асинхронно, время выполнения: {time.time() - start_time:.2f} секунд, '
          f'сумма = {result:_}')
