# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task While 11

import random
N = random.randrange(2,200)
#N = 2
print('N = ', N)
K = 1
S = 1
while S < N:
    K += 1
    S += K
    print("K = {0}, S = {1}".format(K,S))
print()
print("K = {0}, S = {1}".format(K,S))