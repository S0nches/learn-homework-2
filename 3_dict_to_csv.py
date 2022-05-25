"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


import csv
names = [{"age": 18, "name": 'Ann', "job": 'SMM'}, {"age": 28, "name": 'Kate', "job": 'Finance'}]

with open('exp.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ["age", "name", "job"]
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in names:
        writer.writerow(user)