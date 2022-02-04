# A twin prime is a prime number that differs from another prime number by 2.
# Write a function named is_twin_prime which takes an int parameter and
# returns true if it is a twin prime, else false.
# given 5, which is prime
# 5 + 2 = 7, which is prime
# 5 - 2 = 3, which is prime
# hence, 5 has two prime twins and it is a Twin Prime.


def is_twinprime(n):
    res1 = True
    res2 = True
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        else:
            for x in range(3, int((n - 2) ** 0.5) + 1, 2):
                if (n - 2) % x == 0:
                    res1 = False
            for y in range(3, int((n - 2) ** 0.5) + 1, 2):
                if (n - 2) % y == 0:
                    res2 = False

    return res1 or res2


print(is_twinprime(5691))
