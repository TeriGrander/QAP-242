def apply_function(lst, func):
    return [func(i) for i in lst]
    


numbers = [1, 2, 3, 4, 5]
print(apply_function(numbers, lambda x: x**2))
# [1, 4, 9, 16, 25]