# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task Boolean 11

import random
A = random.randrange(1,10)
B = random.randrange(1,10)
print("A = ", A)
print("B = ", B)
a1 = (A%2)==0
b1 = (B%2)==0
x = (a1 == b1)
print("A четно: ", a1)
print("B четно: ", b1)
print("У чисел A и B одинаковая четность: ", x)