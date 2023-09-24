string = str(input("Enter string(MINIMUM - 3 SYMBOLS): "))

while (len(string) < 3):
    string = str(input("Enter string again(MINIMUM - 3 SYMBOLS): "))

without_last = string[:-1]

cut = without_last[::-1]

print(f"A string without the last character and with reverberation - {cut}")
