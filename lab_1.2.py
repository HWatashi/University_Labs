for_month = 50
print("The student receives a scholarship", for_month, "UAH")
spendings = 80
print("Also the student has a total monthly expense of", spendings, "UAH which increases every month by 2 percent")
general = 0

for i in range (10):
    general += spendings
    spendings += (2 / 100) * spendings

print("In 10 months the student spent %.2f UAH" % general)
print("In 10 months the student received", for_month * 10, "UAH" )
print("So the student must take a loan for %.2f UAH" % (general - for_month * 10))
