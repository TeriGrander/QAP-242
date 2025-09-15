def is_valid_email(email):
    if ' ' in email: return False
    elif '@' in email:
        if len(email.split('@')) > 2: return False
        else:
            domain = email.split('@')[1]
            if '.' in domain: return True
            else: return False
    else:
        return False
    
print(is_valid_email('me@my.email'))
print(is_valid_email('me@my'))
print(is_valid_email('check_this'))
print(is_valid_email('and check this'))
print(is_valid_email('me@my@mail.com'))
print(is_valid_email('me@my.mail.com'))
