import time
from typing import Callable

def time_it(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f"Execution time of '{func.__name__}': {int(work_time)} seconds")
        return res
    return wrapper


# Функция — пример
# Она просто делает копию списка, добавляет value в конец списка и возвращает этот список
def add_point(original_list: list, value):
    # Специально делаем sleep, потому как без него время выполнения будет около нуля
    time.sleep(1)
    return original_list[:].append(value)

# Делаем новую функцию уже с декоратором
@time_it
def add_point_with_timer(original_list: list, value):
    add_point(original_list, value)

# Выполняем функцию с декоратором
add_point_with_timer([1, 2, 3, 4, 5], 6)

# Execution time of 'add_point_with_timer': 2.003331 seconds