def common_products(m, store_assortments):
  A = set(store_assortments[0])

  for i in range(1, m):
    current_store_assortment = set(store_assortments[i])
    A = A.intersection(current_store_assortment)

  if not A:
    A = list(store_assortments[0])
    for i in range(1, m):
      A = [product for product in A if product in store_assortments[i]]
    A.sort()
    A = set(A)

  return A


m = 3
store_assortments = [["apple", "banana", "orange", "grape"],
                     ["banana", "grape", "watermelon", "kiwi"],
                     ["apple", "banana", "grape", "strawberry"]]

print("Асортимент 3 магазинів:")
for r in store_assortments:
  print(r)
print()

result = common_products(m, store_assortments)
print("Асортимент, який є в усіх магазинах:", result)    
