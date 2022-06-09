# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task if 11

import random
A = random.randrange(-3,3)
B = random.randrange(-3,3)
print("Число A:", A)
print("Число B:", B)
if A != B:
    A = B = max(A,B)
else:
    A = B = 0
print("Число A:", A)
print("Число B:", B)