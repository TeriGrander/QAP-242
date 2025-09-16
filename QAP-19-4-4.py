import random

def generate_test_data(n=5, min_value=1, max_value=10):
    list_res = []
    for i in range(n):
        list_res.append(random.randint(min_value, max_value))
    return list_res

print(generate_test_data())
print(generate_test_data(n=3, min_value=-5, max_value=5))
