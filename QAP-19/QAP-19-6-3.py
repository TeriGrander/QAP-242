def sort_by_age(lst):
    return sorted(lst, key = lambda tuple_elem: tuple_elem[1], reverse=False)


people = [("Anna", 23), ("John", 21), ("Alice", 25)]
print(sort_by_age(people))

# [('John', 21), ('Anna', 23), ('Alice', 25)]