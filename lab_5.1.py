n = int(input("Enter n for array size:"))
odd = 0
count = 0
print(f"Enter {n} array elements:")

array = [int(input()) for _ in range(n)]

print("Original array: ", array)

s_array = []
nn = n
j = 0
while (nn != 0):
    nn -= 1
    if (array[nn] < 0):
        s_array.append(array[nn])
        count += 1
        j += 1 
if count > 0:
    print("Negative elements in reverse order", s_array)
else:
    print("There are no negative elements in the array")
    
s_count = 0
for i in range(n):
    if (array[i] % 2 != 0):
        odd += array[i]
        s_count += 1
if s_count > 0:
    odd /= s_count
    print(f"The arithmetic mean of the odd elements of the array: {odd}")
else:
    print("There are no odd elements in the array")
