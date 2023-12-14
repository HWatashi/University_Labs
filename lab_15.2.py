import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_frame.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Total'] = df.iloc[:, 1:].sum(axis=1)

choice = input("Введіть 'graph' для виводу графіка або 'dataframe' для виводу DataFrame з даними: ")

if choice.lower() == 'graph':
    
    monthly_data = df.groupby(df['Date'].dt.to_period('M'))['Total'].sum()

    most_popular_month = monthly_data.idxmax()

    plt.figure(figsize=(10, 6))
    monthly_data.plot(kind='bar', color='skyblue')
    plt.title('Загальна кількість велосипедистів за місяцями')
    plt.xlabel('Місяці')
    plt.ylabel('Загальна кількість велосипедистів')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print(f"Найбільш популярний місяць для велосипедистів: {most_popular_month}")

elif choice.lower() == 'dataframe':
    
    print(df)

else:
    print("Введено неправильний вибір. Будь ласка, виберіть 'graph' або 'dataframe'.")
