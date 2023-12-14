import matplotlib.pyplot as plt
import json

def find_positions(file_name):
    # Функція з лабораторної №12 для знаходження топ-3 команд
    data = load_data(file_name)
    if data:
        sorted_data = sorted(data, key=lambda x: x['очки'], reverse=True)
        top_3 = sorted_data[:3]
        return top_3

def load_data(file_name):
    # Завантаження даних з файлу JSON
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

def create_pie_chart(data):
    # Побудова кругової діаграми на основі отриманих даних
    labels = [team['назва'] for team in data]
    sizes = [team['очки'] for team in data]
    colors = ['gold', 'lightskyblue', 'lightcoral']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.title('Розподіл очок серед топ-3 команд')
    plt.show()

def main():
    file_name = 'football_scores.json'
    top_3_teams = find_positions(file_name)
    if top_3_teams:
        create_pie_chart(top_3_teams)

if __name__ == "__main__":
    main()

