import json


def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None


def display_data(file_name):
    data = load_data(file_name)
    if data:
        print(json.dumps(data, indent=4, ensure_ascii=False))


def create_initial_file(file_name):
    initial_data = [
        {"назва": "Команда 1", "очки": 20},
        {"назва": "Команда 2", "очки": 18},
        {"назва": "Команда 3", "очки": 15},
        {"назва": "Команда 4", "очки": 12},
        {"назва": "Команда 5", "очки": 10},
        {"назва": "Команда 6", "очки": 8},
        {"назва": "Команда 7", "очки": 6},
        {"назва": "Команда 8", "очки": 5},
        {"назва": "Команда 9", "очки": 3},
        {"назва": "Команда 10", "очки": 1}
    ]
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(initial_data, file, indent=4, ensure_ascii=False)
    print(f"Створено початковий файл з даними: {file_name}")


def add_team_score(file_name, team_name, points):
    data = load_data(file_name)
    if data:
        new_team = {"назва": team_name, "очки": points}
        data.append(new_team)
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Запис {team_name} з кількістю очок {points} додано.")


def remove_team(file_name, team_name):
    data = load_data(file_name)
    if data:
        updated_data = [team for team in data if team['назва'] != team_name]
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, indent=4, ensure_ascii=False)
        print(f"Запис {team_name} видалено.")
    else:
        print(f"Команди {team_name} немає у файлі.")


def search_by_team_name(file_name, team_name):
    data = load_data(file_name)
    if data:
        found_teams = [team for team in data if team['назва'] == team_name]
        if found_teams:
            print(f"Команда: {found_teams[0]['назва']}, Кількість очок: {found_teams[0]['очки']}")
        else:
            print(f"Команди {team_name} немає у файлі.")


def find_positions(file_name):
    data = load_data(file_name)
    if data:
        sorted_data = sorted(data, key=lambda x: x['очки'], reverse=True)
        champion = sorted_data[0]['назва']
        second_place = sorted_data[1]['назва']
        third_place = sorted_data[2]['назва']
        return champion, [second_place, third_place]


def save_results(file_name, result_file):
    champion, places = find_positions(file_name)
    results = {
        "Чемпіон": champion,
        "Друге місце": places[0],
        "Третє місце": places[1]
    }
    with open(result_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
    print(f"Результати збережено у файлі {result_file}.")


def main():
    file_name = 'football_scores.json'
    result_file = 'football_results.json'

    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        create_initial_file(file_name)

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Пошук за назвою команди")
        print("5. Знайти чемпіона, друге і третє місце")
        print("6. Зберегти результати у новий JSON файл")
        print("7. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            display_data(file_name)
        elif choice == '2':
            team_name = input("Введіть назву команди: ")
            points = int(input("Введіть кількість очок: "))
            add_team_score(file_name, team_name, points)
        elif choice == '3':
            team_name = input("Введіть назву команди для видалення: ")
            remove_team(file_name, team_name)
        elif choice == '4':
            team_name = input("Введіть назву команди для пошуку: ")
            search_by_team_name(file_name, team_name)
        elif choice == '5':
            result = find_positions(file_name)
            if result:
                champion, places = result
                print(f"Чемпіон: {champion}")
                print(f"Друге місце: {places[0]}")
                print(f"Третє місце: {places[1]}")
        elif choice == '6':
            save_results(file_name, result_file)
        elif choice == '7':
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
