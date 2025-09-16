def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    if len(password) < min_length: return False
    elif require_upper and (password.islower() or password.isnumeric()): return False
    elif require_lower and (password.isupper() or password.isnumeric()): return False
    elif require_digit and password.isalpha(): return False
    else: return True
    