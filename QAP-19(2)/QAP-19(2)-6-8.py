import time

def timer():
    last_call = time.time()
    def time_checker():
        x = time.time()
        nonlocal last_call
        elapsed = x - last_call
        last_call = x
        return elapsed
    return time_checker

my_timer = timer()
print(int(my_timer())) # int — для приближенного значения секунд
# Ждем немного...
time.sleep(2)
print(int(my_timer()))

# Вывод:
# 0
# 2