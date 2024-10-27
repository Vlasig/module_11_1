import requests
import numpy as np
import pandas as pd


def get_data(url):
    response = requests.get(url)
    print(response.json())


print("\n библиотека requests \n")
get_data('https://api.github.com')

data = pd.read_csv('data.csv')
print("\n библиотека pandas \n")

print(data.head())

average = data['column_name'].mean()
print(f'Среднее значение столбца "column_name": {average}')

numbers = np.array([1, 2, 3, 4, 5])
print("\n библиотека numpy \n")

print(numbers)

sum = np.sum(numbers)
mean = np.mean(numbers)
max_value = np.max(numbers)
min_value = np.min(numbers)

print(f'Сумма элементов массива: {sum}')
print(f'Среднее значение массива: {mean}')
print(f'Максимальное значение в массиве: {max_value}')
print(f'Минимальное значение в массиве: {min_value}')
