def binary_search(lst, item):
    if len(lst) == 0: return False
    mid = len(lst) // 2
    if item == lst[mid]: return True
    elif item < lst[mid]: return binary_search(lst[:mid], item)
    else: return binary_search(lst[mid+1:], item)

print(binary_search([1, 2, 3, 4, 5], 4))
# True
print(binary_search([1, 2, 3, 4, 5], 6))
print(binary_search([1, 2, 3, 4, 5, 6], 2))
print(binary_search([1, 2, 3, 4, 5, 6], 8))
# False


print(binary_search(['apple', 'banana', 'cherry'], 'date'))