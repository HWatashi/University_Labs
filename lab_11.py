def read_csv_file(file_name):
  try:
    with open(file_name, 'r', encoding='utf-8') as file:
      data = file.readlines()
      return [line.strip() for line in data]
  except FileNotFoundError:
    print(f"Файл '{file_name}' не знайдено.")
    return None


def filter_inflation_data(data, threshold):
  filtered_data = []
  header_skipped = False

  for line in data:
    if not header_skipped:
      header_skipped = True
      continue

    values = line.split(',')
    if len(values) >= 4 and values[3].strip():
      try:
        inflation = float(values[3])
        if inflation > threshold:
          filtered_data.append(line)
          print(line)
      except ValueError:
        line = line

  return filtered_data


def write_filtered_data_to_csv(filtered_data, output_file):
  try:
    with open(output_file, 'w', encoding='utf-8') as file:
      for line in filtered_data:
        file.write(line + '\n')
    print(f"Результати збережено у файлі '{output_file}'")
  except PermissionError:
    print(
        f"Неможливо записати у файл '{output_file}'. Перевірте права доступу.")


def main():
  input_file = 'data.csv'
  data = read_csv_file(input_file)

  if data:
    print("Дані з вхідного файлу:")
    print('\n'.join(data[1:]))

    try:
      threshold = float(
          input("Введіть значення інфляції, від якого шукати дані: "))
    except ValueError:
      print("Будь ласка, введіть числове значення.")
      return

    filtered_data = filter_inflation_data(data, threshold)

    if filtered_data:
      output_file = 'filtered_data.csv'
      write_filtered_data_to_csv(filtered_data, output_file)
    else:
      print("Немає даних, що задовольняють вашу умову.")


if __name__ == "__main__":
  main()
