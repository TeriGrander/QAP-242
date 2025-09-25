def is_palindrome(s):
    if len(s) <= 1: return True
    elif len(s) == 2 and s[0] == s[-1]: return True
    elif len(s) == 2 and s[0] != s[-1]: return False
    else: return is_palindrome(s[1:-1])

print(is_palindrome('a'))
print(is_palindrome(''))
print(is_palindrome('aa'))
print(is_palindrome('racecar'))
# True
print(is_palindrome('gong'))
# False