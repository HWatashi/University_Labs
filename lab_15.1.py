import pandas as pd

data = {
    'Store 1': ["apple", "banana", "orange", "grape"],
    'Store 2': ["banana", "grape", "watermelon", "kiwi"],
    'Store 3': ["apple", "banana", "grape", "strawberry"]
}

df = pd.DataFrame(data)

df = df.transpose()

df.columns = ['Item 1', 'Item 2', 'Item 3', 'Item 4']

result = df.melt(var_name='Store', value_name='Item') \
          .groupby('Item')['Store'] \
          .value_counts() \
          .unstack(fill_value=0)

print(result) 
