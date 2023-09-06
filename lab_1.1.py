a = int(input ("Enter a in range(from 1 to 100): "))

while (a < 1 or a > 100):

    a = int(input ("Enter again please a in range (from 1 to 100): "))

b = int(input ("Enter b in range (from 1 to 100): "))

while (b < 1 or b > 100):

    b = int(input ("Enter again b in range (from 1 to 100): "))

if a > b:

    r = (2 * a) / b + 1

elif a == b:

    r = -445

else:

    r = (b + 5) / a

print("Calculation result: " , r)
