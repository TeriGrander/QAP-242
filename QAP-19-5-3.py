def check_data_format(**kwargs):
    result = True
    for (key, data) in kwargs.items():
        if not isinstance(key, str): 
            result = False
            break
        elif not isinstance(data, (int, float)):
            result = False
            break
    return result


print(check_data_format(uid=24891, age=30, height=180))
print(check_data_format(uid=24191, age="30", height=156))
print(check_data_format(uid=24191, age=30, height="156"))
print(check_data_format(uid="24191", age=30, height=156))