def sort_strings_by_last_char(strings):
    return sorted(strings, key = lambda string: string[-1], reverse=False)


strings = ["apple", "banana", "cherry1", "date", "elderberry"]
print(sort_strings_by_last_char(strings))
# ['banana', 'apple', 'date', 'cherry', 'elderberry']