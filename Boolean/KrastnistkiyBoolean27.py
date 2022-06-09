# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task Boolean 27

import numpy as np
x,y = list(np.random.choice(range(-10, 11), 2))
print("x = {0}, y = {1}".format(x,y))
b = (x < 0)
print("Точка лежит во 2-й или 3-й координатной четверти: ", b)