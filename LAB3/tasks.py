import pandas as pd
from matplotlib import pyplot as plt

# task1(Оптимизировать вывод)
df = pd.read_csv('sales.csv')
print(df.head(15), df.tail(15))

# task2
print(df.shape[0])

# task3
print(df.info(show_counts=False))

# task4
print(df['Global_Sales'].describe()['max'], df['Global_Sales'].describe()['mean'])

# task5
print(df.isnull().sum())
df[df.select_dtypes(include=["float", "int"]).columns] = df[df.select_dtypes(include=["float", "int"]).columns].fillna(
    df[df.select_dtypes(include=["float", "int"]).columns].median())
df.dropna(subset=df.select_dtypes(exclude=["float", "int"]).columns, inplace=True)

# task6
genres = df['Genre'].value_counts()
print(genres.idxmax())
plt.pie(genres, labels=genres.index)
plt.show()

# task7
g = df['Platform'].value_counts()
print(g.idxmax())
plt.xticks(rotation='vertical')
plt.bar(g.index, g.values)
plt.show()

# task8
years = df['Year'].value_counts().sort_index()
plt.bar(years.index, years.values)
plt.xticks(ticks=years.index, rotation='vertical')
plt.show()

# task9
sales = df.groupby('Year')['Global_Sales'].sum()
print(sales.idxmax())
plt.bar(sales.index, sales.values)
plt.xticks(ticks=sales.index, rotation='vertical')
plt.show()

# task10(Задание выполнено неверно, круги 'наслаиваются' друг на дурга, а не суммируются в результате чего мы
# получаем не объем продаж, а максимальное число продаж за еденицу времени)
plt.figure(figsize=(10, 5))
plt.scatter(x=df['Platform'], y=df['Genre'], s=df['Global_Sales'] * 3)
plt.xticks(rotation='vertical')
plt.show()

# task11
sales = df[df['Genre'] == 'Shooter'].groupby('Year')['JP_Sales'].sum()
print(sales.idxmax())
plt.plot(sales.index, sales.values)
plt.xticks(ticks=sales.index, rotation='vertical')
plt.show()

# task12
print(df[df['Year'] == df['Year'].min()]['Name'].to_string(index=False))

# task13
print(df[(df['Genre'] == 'Shooter') & (df['Year'] == 2003)]['Name'].count())
