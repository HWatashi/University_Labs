def print_dict_values(dictionary):
  print("Значення словника:")
  for key, value in dictionary.items():
    print(f"{key}: {value}")


def add_record(dictionary, key, value):
  if key in dictionary:
    raise ValueError("Запис вже існує. Введіть інший ключ.")
  dictionary[key] = value
  print(f"Запис додано: {key}: {value}")


def remove_record(dictionary, key):
  if key not in dictionary:
    raise KeyError("Ключ не знайдено. Введіть інший ключ.")
  del dictionary[key]
  print(f"Запис з ключем {key} видалено.")


def main():
  football_teams = {
      'Team1': 25,
      'Team2': 30,
      'Team3': 28,
      'Team4': 20,
      'Team5': 35,
      'Team6': 18,
      'Team7': 29,
      'Team8': 31,
      'Team9': 22,
      'Team10': 33
  }

  while True:
    print("\nМеню:")
    print("1. Вивести значення словника")
    print("2. Додати запис до словника")
    print("3. Видалити запис зі словника")
    print("4. Відсортувати та вивести словник за ключами")
    print("5. Завершити програму й вивести перші три місця за кількістю голів")

    choice = input("Виберіть опцію (1/2/3/4/5): ")

    if choice == '1':
      print_dict_values(football_teams)
    elif choice == '2':
      key = input("Введіть ключ: ")
      value = int(input("Введіть значення: "))
      try:
        add_record(football_teams, key, value)
      except ValueError as e:
        print(f"Помилка: {e}")
    elif choice == '3':
      key = input("Введіть ключ для видалення: ")
      try:
        remove_record(football_teams, key)
      except KeyError as e:
        print(f"Помилка: {e}")
    elif choice == '4':
      sorted_keys = sorted(football_teams,
                           key=lambda x: football_teams[x],
                           reverse=True)
      print("Вміст словника за відсортованими ключами:")
      for key in sorted_keys:
        print(f"{key}: {football_teams[key]}")
    elif choice == '5':
      break
    else:
      print("Невірний вибір. Спробуйте ще раз.")
  sorted_keys = sorted(football_teams,
                       key=lambda x: football_teams[x],
                       reverse=True)
  champion = sorted_keys[0]
  second_place = sorted_keys[1]
  third_place = sorted_keys[2]

  print(f"Чемпіон: {champion}")
  print(f"Друге місце: {second_place}")
  print(f"Третє місце: {third_place}")

if __name__ == "__main__":
  main()
