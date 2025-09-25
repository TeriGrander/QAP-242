import random

def generate_user_data(size, names, surnames, age_range):
    for i in range(size):
        name = names[random.randrange(0,len(names))]
        surname = surnames[random.randrange(0,len(surnames))]
        age = random.randrange(age_range[0],age_range[1])
        yield name, surname, age

first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)