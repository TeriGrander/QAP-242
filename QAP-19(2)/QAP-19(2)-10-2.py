from typing import List, Dict, Tuple, Any

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    return list(map(lambda x: f"{x['first_name']} {x['last_name']}", users))

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    email_list1 = list(map(lambda x: x['email'], users1))
    email_list2 = list(map(lambda x: x['email'], users2))
    return set(list(filter(lambda x: x in email_list2, email_list1)))

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, Tuple[Any]]:
    keys = users[0].keys()
    first_names = list(map(lambda x: x['first_name'], users))
    last_names = list(map(lambda x: x['last_name'], users))
    birth_dates = list(map(lambda x: x['birth_date'], users))
    emails = list(map(lambda x: x['email'], users))
    res = dict(zip(keys, [first_names, last_names, birth_dates, emails]))
    return res


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
             {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
             {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]

print(convert_to_full_name(users_data))
# ['John Doe', 'Bob Johnson', 'Lev Sergeev']
print(find_matching_emails(users_data, users_data_ext))
# {'johndoe@gmail.com'}
print(combine_user_data(users_data))
# {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')}