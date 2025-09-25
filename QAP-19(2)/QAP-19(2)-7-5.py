import time, random

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'Function {func.__name__} took {int(work_time)} seconds to run')
        return res
    return wrapper

@time_it
def test_function():
    x = random.randint(1,4)
    time.sleep(x)

test_function()
# Function test_function took 2 seconds to run

test_function()
test_function()
test_function()