def add_elements_with_odd_indices(input_list):
  new_elements = input("Введіть елементи для додавання через пробіл: ").split()

  for i in range(1, len(new_elements), 2):
    input_list.append(new_elements[i])

  print("Оновлений список:", input_list)


my_list = [1, 2, 3, 4, 5]
print("Початковий список: ", my_list)
add_elements_with_odd_indices(my_list)
