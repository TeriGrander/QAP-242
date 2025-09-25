def fibonacci1(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci(n):
    i = 0
    n1 = 0
    n2 = 1
    while i < n:
       if i == 0: yield 0
       elif i == 1: yield 1
       else:
            yield n1 + n2
            n1, n2 = n2, n1 + n2
       i += 1


test1 = list(fibonacci(15))
print(test1)

print('another way')
for i in range(15):
    print(fibonacci1(i), end = ', ')