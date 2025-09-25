def create_unique_checker():
    checked = set([])
    def checker(x):
        if x not in checked: 
            checked.add(x)
            return True
        else: return False
    return checker

unique_checker = create_unique_checker()
print(unique_checker(5))  
print(unique_checker(5))  
print(unique_checker(10))  