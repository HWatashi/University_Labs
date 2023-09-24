words = str(input("Enter words(Ukrainian): "))

words_space = words.split() 
ivent = False

print("Let`s find words that end with 'ий'")

for word in words_space:
    if word.endswith("ий"):
        print(word)
        ivent = True
if (ivent == False):
    print("No words found ending with 'ий'") 
