def compare_lists(list1, list2, ignore_case=False):
    list_res = []
    list1_temp = []
    list2_temp = []
    if ignore_case:
        for i in(range(len(list1))):
            if isinstance(list1[i], str): 
                list1_temp.append(list1[i].casefold())
            else: list1_temp.append(list1[i])
        for i in(range(len(list2))):
            if isinstance(list2[i], str): 
                list2_temp.append(list2[i].casefold())
            else: list2_temp.append(list2[i])
    else:
        list1_temp = list1.copy()
        list2_temp = list2.copy()
    for i in range(len(list1_temp)):
        if list1_temp[i] not in list2_temp: list_res.append(list1_temp[i])
    return list_res

print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))
# ["apple", "banana"]
print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"], ignore_case=True))
# ["apple"]
print(compare_lists(["apple", "banana", "cherry", 5, 6], ["Banana", "cherry", "date"], ignore_case=True))