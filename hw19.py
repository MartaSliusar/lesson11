def is_prime(n):
    for i in range(2, n):
        if n <= 1:
            return False
        if n % i == 0:
            return False
    return True
def prime_generator(number):
    n = 2
    while n <= number:
        if is_prime(n):
            yield n
        n += 1
