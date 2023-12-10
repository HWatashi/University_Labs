def create_file(file_name):
  try:
    with open(file_name, 'w') as file:
      file.write(
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      )
    print(f"File {file_name} created successfully!")
  except IOError:
    print(f"Error creating file {file_name}.")


def find_longest_words(file_name):
  try:
    with open(file_name, 'r') as file:
      content = file.read().split()
      content = [word.strip(",.?!") for word in content]
      content.sort(key=len, reverse=True)
      unique_longest_words = []
      for word in content:
        if word not in unique_longest_words and len(unique_longest_words) < 5:
          unique_longest_words.append(word)

      with open('TF20_2.txt', 'w') as output_file:
        output_file.write(' '.join(unique_longest_words))

      print(f"Five unique longest words written to TF20_2.txt")
  except IOError:
    print(f"Error reading or writing files.")


def print_words_in_groups_of_five(file_name):
  try:
    with open(file_name, 'r') as file:
      content = file.read().split()
      for i in range(0, len(content), 5):
        print(' '.join(content[i:i + 5]))
  except IOError:
    print(f"Error reading file {file_name}.")


# a) Створення текстового файлу TF20_1
file1_name = "TF20_1.txt"
create_file(file1_name)

# б) Знаходження та запис п'ятьох різних найдовших слів у файл TF20_2
find_longest_words(file1_name)

# в) Виведення вмісту файлу TF20_2 по п'ять слів у рядок
print("Content of TF20_2.txt:")
print_words_in_groups_of_five('TF20_2.txt')
