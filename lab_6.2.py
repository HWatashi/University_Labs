def find_surrounding_elements(input_list, target_element):
  surrounding_elements = []
  for i in range(len(input_list)):
    if input_list[i] == target_element:
      if i > 0:
        surrounding_elements.append(input_list[i - 1])
      if i < len(input_list) - 1:
        surrounding_elements.append(input_list[i + 1])
      break

  return surrounding_elements


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Початковий список: ", my_list)
target_element = int(input("Введіть елемент, який потрібно знай): "))
result = find_surrounding_elements(my_list, target_element)
if result:
  print(f"Елементи, що оточують {target_element}: {result}")
else:
  print(
      f"{target_element} не знайдено у списку або немає оточуючих елементів.")
