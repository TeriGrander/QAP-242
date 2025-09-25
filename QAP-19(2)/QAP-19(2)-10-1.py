import datetime
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    age = 0
    birthdate_lst = birth_date.split('-')
    birthdate_date = datetime.date(int(birthdate_lst[0]), int(birthdate_lst[1]), int(birthdate_lst[2]))
    date_now = datetime.date(datetime.datetime.now().year,
                             datetime.datetime.now().month,
                             datetime.datetime.now().day)
    delta_days = (date_now - birthdate_date).days
    if delta_days // 365 >=4:
        leaps = (delta_days // 365) // 4
        age = (delta_days - leaps * 365) // 365 + leaps
    else:
        age = delta_days // 365
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return list(filter(lambda user: calculate_age(user['birth_date']) >= 18, users))

def generate_username(first_name: str, last_name: str) -> str:
    return first_name.casefold()[0] + '.' + last_name.casefold()

print(calculate_age('2023-06-19'))
print(calculate_age("1990-05-15"))
users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]

print(filter_adults(users_data))
# [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}]
print(generate_username("John", "Doe"))
# "j.doe"