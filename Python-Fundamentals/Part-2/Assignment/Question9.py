#  Write a function is_prime(n) that returns True if is a prime number and False otherwise, using a loop.

import math

def is_prime(n):
    is_prime = True

    if n <= 1:
        is_prime = False
    elif n == 2:
        is_prime = True
    elif n % 2 == 0:
        is_prime = False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                is_prime = False
                break

    return is_prime

print(is_prime(7))