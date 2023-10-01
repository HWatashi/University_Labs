n = 7

array = []

for i in range(n):
    row = []
    for j in range(n):
        if (j + 1) % 2 != 0:
            row.append(1)
        else:
            row.append(0)
    array.append(row)

for r in array:
    print(*r)
