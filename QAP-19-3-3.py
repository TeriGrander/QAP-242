def is_success_code(code):
    if 200 <= int(code) <= 299: return True
    else: return False