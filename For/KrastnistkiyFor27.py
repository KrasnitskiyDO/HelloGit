# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task For 27

import math
X = 0.9
N = 100
print('X = ', X)
print('N = ', N)
p = X
S = X
k = 1
for i in range(1,N+1):
    p *= k/((k+1)*(k+2)) * X*X
    S += p
    print(i," : ",k," : ",p," : ",S)
    k += 2
    p *= k
print("Result:")
print(S)
print("asin(x):")
print(math.asin(X))