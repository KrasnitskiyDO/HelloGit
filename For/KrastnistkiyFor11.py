# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task For 11

import random
N = random.randrange(10)
print('N = ', N)
S = 0.0
for i in range(N,2*N+1):
    x = i**2
    S += x
    print(i," : ",x," : ",S)
print("Sum = ",S)