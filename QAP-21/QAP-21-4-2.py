class PasswordChecker:
    min_len = 0
    max_len = 0
    def set_password_range(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len
    
    def check_passwords(self, pass_list):
        result = []
        for i in pass_list:
            if self.min_len <= len(i) <= self.max_len: result.append(True)
            else: result.append(False)
        return result
    
checker1 = PasswordChecker()
checker1.set_password_range(5, 10)
print(checker1.min_len, checker1.max_len)

# 5 10

print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))  

# [False, True, False]