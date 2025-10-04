class User:
    private_key = ''
    def set_private_key(self, key):
        self.private_key = key
    
    def show_private_key(self):
        print(f'Приватный ключ пользователя: {self.private_key}')
    
user1 = User()
user1.set_private_key('uox00b_12x')
user1.show_private_key()  