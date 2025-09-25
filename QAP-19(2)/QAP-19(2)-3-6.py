def is_prime(n):
    for i in range(2,n):
        if n % i == 0: return False
    return True

def primes(n):
    for i in range(2, n+1):
        if is_prime(i): yield i
        else: continue


# print(is_prime(9))
# print(is_prime(3))
# print(is_prime(17))


prime_generator = primes(1)
for prime in prime_generator:
   print(prime)