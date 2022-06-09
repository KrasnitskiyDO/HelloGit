# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task if 27

import math
x = -1
while x < 11:
    x_floor = math.floor(x)
    if x < 0:
        y = 0
    elif x_floor%2 == 0:
        y = 1
    else:
        y = -1
    print("x = {0} : f(x) = {1}".format(x,y))
    x += .5