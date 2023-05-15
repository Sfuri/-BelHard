# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('Gsales.csv')

# Вывод первых и последних строк данных
print(df.head(), '\n')
print(df.tail(), '\n')

# Проверка типов данных в столбцах
print(df.dtypes, '\n')


# Функция для определения столбцов с типом данных, отличным от object
def column_type_is_not_object(df):
    new_list = []
    for column in df.columns:
        if df[column].dtype != object:
            new_list.append(column)
    return new_list


# Вывод размера датафрейма, количества дубликатов и пропущенных значений
print(df.shape, '\n')
print(df.duplicated().sum(), '\n')
print(df.isnull().sum(), '\n')
print(df.count(), '\n')

# Удаление строк с пропущенными значениями и изменение типа данных столбцов float на int
df = df.dropna()
for col in df.select_dtypes(include='float'):
    df[col] = df[col].astype(int)

# Вывод типов данных столбцов после изменений
print(df.dtypes, '\n')
print(df.count(), '\n')


# Функция для построения boxplot для столбцов с числовыми значениями
def boxplot_of_columns(df):
    for col in df.select_dtypes(include=np.number).columns:
        sns.boxplot(x=df[col], color='orange')
        plt.title(f'Boxplot столбца {col}')
        plt.xlabel('Значения')
        plt.ylabel('Столбец')
        plt.show()


# Построение boxplot для исходного датафрейма
boxplot_of_columns(df)

# Создание копии датафрейма без выбросов
df_without_outliers = df.copy(deep=True)


# Фильтрация выбросов в данных
def filter_outliers(df):
    for col in column_type_is_not_object(df):
        q_low = df[col].quantile(0.01111)
        q_hi = df[col].quantile(0.99999)
        df = df[(df[col] >= q_low) & (df[col] <= q_hi)]
    return df


df = filter_outliers(df)

# Построение boxplot для датафрейма без выбросов
boxplot_of_columns(df)

# Создание столбца 'sales_by_year', содержащего суммарные продажи за год
df_without_outliers['sales_by_year'] = df_without_outliers.groupby('Year')['Global_Sales'].sum()

# Построение столбчатой диаграммы для суммарных продаж по годам
sns.barplot(data=df_without_outliers, x='Year', y='sales_by_year', palette='viridis', errorbar=None)
plt.title('Суммарные продажи по годам')
plt.xlabel('Год')
plt.ylabel('Суммарные продажи')
plt.show()

# Построение гистограммы для распределения жанров
sns.histplot(data=df, x='Genre')
plt.title('Распределение жанров')
plt.xlabel('Жанр')
plt.ylabel('Количество игр')
plt.show()

# Создание столбцов для суммарных продаж по жанрам и категориям продаж
for category in ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'):
    column_name = f'genre_{category}'
    df_without_outliers[column_name] = df_without_outliers.groupby('Genre')[category].transform('sum')
    sns.barplot(data=df_without_outliers, x='Genre', y=column_name, palette='viridis')
    plt.title(f'Суммарные продажи по жанрам ({category})')
    plt.xlabel('Жанр')
    plt.ylabel('Суммарные продажи')
    plt.show()

# Создание столбца 'Games_Count', содержащего количество выпущенных игр определенного жанра за год
df_without_outliers['Games_Count'] = df_without_outliers.groupby(['Genre', 'Year'])['Name'].transform('count')

# Создание корреляционной матрицы и построение тепловой карты
plt.figure(figsize=(12, 8))
pivot_table = df_without_outliers.pivot_table(index='Year', columns='Genre', values='sales_by_year', aggfunc='sum')
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=0.5)
plt.title('Корреляция между годом, количеством игр определенного жанра и продажами за год')
plt.xlabel('Жанр')
plt.ylabel('Год')
plt.show()
