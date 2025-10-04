class User:
    def __init__(self, email, password, balance) -> None:
        self.email = email
        self.password = password
        self.balance = balance
    
    def login(self, email, password):
        return email == self.email and password == self.password
    
    def update_balance(self, amount):
        self.balance += amount

user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
print(user.balance)
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700