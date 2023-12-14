import matplotlib.pyplot as plt

file_path = 'data_age.csv'

with open(file_path, 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]

years = header[4:]

ukraine_values = [float(row[i]) for row in data if row[2] == 'Ukraine' for i in range(4, len(row))]
austria_values = [float(row[i]) for row in data if row[2] == 'Austria' for i in range(4, len(row))]

def plot_countries_dynamic():
    plt.figure(figsize=(10, 6))
    plt.plot(years, ukraine_values, label='Ukraine')
    plt.plot(years, austria_values, label='Austria')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника % населення працездатного віку')
    plt.title('Динаміка показників для України та Австрії')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_country_bar(country_name):
    country_values = [float(row[i]) for row in data if row[2] == country_name for i in range(4, len(row))]
    
    plt.figure(figsize=(10, 6))
    plt.bar(years, country_values, color='skyblue')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника % населення працездатного віку')
    plt.title(f'Динаміка показника для {country_name}')
    plt.grid(axis='y')
    plt.show()

while True:
    print("Оберіть опцію:")
    print("1. Побудувати графік для України та Австрії")
    print("2. Побудувати стовпчасту діаграму для певної країни")
    print("3. Вийти")

    option = input("Введіть номер опції: ")

    if option == "1":
        plot_countries_dynamic()
    elif option == "2":
        country_name_input = input('Введіть назву країни для побудови діаграми: ')
        plot_country_bar(country_name_input)
    elif option == "3":
        print("До побачення!")
        break
    else:
        print("Будь ласка, введіть правильний номер опції.")    
