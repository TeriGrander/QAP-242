def check_password(password):
    if len(password) < 8: print('Пароль должен быть не менее 8 символов')
    if password.islower() or password.isnumeric(): print('Пароль должен содержать хотя бы одну заглавную букву')
    if password.isupper() or password.isnumeric(): print ('Пароль должен содержать хотя бы одну строчную букву')
    if password.isalpha(): print('Пароль должен содержать хотя бы одну цифру')
    