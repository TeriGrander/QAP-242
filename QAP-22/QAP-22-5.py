import random

def choice_sort(lst):
    for i in range(len(lst)-1):
        new = min(lst[i:])
        new_ind = lst.index(new)
        lst[i], lst[new_ind] = lst[new_ind], lst[i]
    return lst

# initial = [random.randint(1, 50) for _ in range(10)]
initial = [43, 45, 8, 4, 28, 17, 33, 49, 11, 24]
print(initial)
sorted_array = choice_sort(initial)
print(sorted_array)