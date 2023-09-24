from mod import is_prime

n = int(input("Enter n: "))
if is_prime(n):
  print("n - prime number")
else:
  print("n is not a prime number")
