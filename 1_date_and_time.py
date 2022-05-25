"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

dt_now = datetime.now()
print(dt_now)

delta = timedelta(days=1)

dt = dt_now - delta
print(dt)

delta2 = timedelta(days=30)

dt2 = dt_now - delta2
print(dt2)

date_string = "01/01/20 12:10:03.234567"

date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)




