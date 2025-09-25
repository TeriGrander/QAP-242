import random

def create_password_generator(length, symbols):
    passwords = set([''])
    def generate_password():
        nonlocal passwords
        password = ''
        while password in passwords:
            password = ''.join(random.choices(symbols, k=length))
        passwords.add(password)
        return password
    return generate_password



symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password_generator = create_password_generator(10, symbols_for_password)

for i in range(10):
    print(password_generator())
print(password_generator())

# Stl0tgwWSL
# oboYrgROdF