def sort_data(**kwargs):
    result = []
    for i in kwargs.keys(): result.append(i)
    result.sort()
    for i in range(len(result)):
        result[i] = (result[i], kwargs[result[i]])
    return result


print(sort_data(name='Alex', age=30, city='New York'))
# [('age', 30), ('city', 'New York'), ('name', 'Alex')]