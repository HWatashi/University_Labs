import math

def calculation(m):
        z = 1 / (math.sqrt(m) + math.sqrt(2))
        print("Result z: ", z)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

m = float(input("Enter m: "))
calculation(m)

n = int(input("Enter n: "))
if is_prime(n):
    print("n - prime number")
else:
    print("n is not a prime number")
