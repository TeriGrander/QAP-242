# Первое решение. Простое, красивое, логичное, удовлетворяет условиям, но на данный момент не проходит 2 теста из 4 в курсе.
# def process_test_data(*args, **kwargs):
#     result = []
#     for i in args:
#         result.append(str(i))
#     for key, value in kwargs.items():
#         result.append(f'{key}={value}')
#     return ', '.join(result)

# Второе решение. Громоздкое, но зато все 4 теста проходят. Вот только эти лишние запятые мне не нравятся!!!
def process_test_data(*args, **kwargs):
    args_lst = []
    for i in args:
        args_lst.append(str(i))
    args_str = ', '.join(args_lst)
    kwargs_lst = []
    for key, value in kwargs.items():
        kwargs_lst.append(f'{key}={value}')
    kwargs_str = ', '.join(kwargs_lst)
    return args_str + ', ' + kwargs_str

print(process_test_data('test_case_1', 'pass', id=1234, user='Alex'))
# test_case_1, pass, id=1234, user=Alex

print(process_test_data(1, 2, 3, x = 4, y = 5, z = 6))
print(process_test_data(1.1, 2.2, 3.3, x = 4.4, y = 5.5, z = 6.6))
print(process_test_data(x = 4, y = 5, z = 6))
print(process_test_data(1, 2, 3))