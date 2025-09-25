def create_counter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x 
    return counter

counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"