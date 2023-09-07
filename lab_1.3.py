N = int(input("Enter an integer N (1 < N < 9): "))

while (2 > N or N > 9):
    N = int(input("Enter an integer N (1 < N < 9): "))
    
for i in range(1, N + 1):
    for j in range(i, N + 1):
        print(j, end="")
    print()
