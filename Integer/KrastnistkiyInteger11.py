# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task Integer 11

import random
N = random.randrange(100,1000)
print("Число: ", N)
d2 = int(N/100)
d1 = int((N-d2*100)/10)
d0 = N%10
print("Сотни: ", d2)
print("Десятки: ", d1)
print("Единицы: ", d0)
print("Сумма цифр: ", d0+d1+d2)
print("Произведение цифр: ", d0*d1*d2)