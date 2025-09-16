def aggregate_data(*args, **kwargs):
    sum = 0
    num = 0
    for i in args:
        if isinstance(i, str):
            num += 1
        elif isinstance(i, (int, float)):
            sum += i
    for i in kwargs.values():
        if isinstance(i, str):
            num += 1
        elif isinstance(i, (int, float)):
            sum += i
    return sum, num


print(aggregate_data(1, 2, 'test1', error_count=3, test_id='test2'))