word = str(input("Enter word(MINIMUM - 3 SYMBOLS): "))

while (len(word) < 3):
    word = str(input("Enter word again(MINIMUM - 3 SYMBOLS): "))

reverb = word[::-1]

print(f"Reversed word - {reverb}")
