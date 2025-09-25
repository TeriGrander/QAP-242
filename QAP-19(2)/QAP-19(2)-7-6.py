import random

def retry_if_result_is_none(times=1):
    def deco(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                x = func(*args, **kwargs)
                if x: return x
            return None
        return wrapper
    return deco
    

@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, "Passed"])

# Получилось получить значение за 2 вызова
print(test_function())
# Passed 

# Не получилось получить значение за 2 вызова
print(test_function())
# None 