def calculate_average(*args):
    sum_args = 0
    for i in args:
        sum_args += i
    return round(sum_args / len(args), 2)

print(calculate_average(1.2, 0.9, 1.3, 1.1, 1.7, 8.4, 0.2))