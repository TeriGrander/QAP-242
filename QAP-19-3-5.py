def test_function(func_name, test_arg, exp_result):
    if func_name(test_arg) == exp_result: return True
    else: return False

def square(n):
    return n ** 2

print(test_function(square, 2, 4))
print(test_function(square, 5, 20))