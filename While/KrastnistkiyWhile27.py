# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task While 27

import random
fib = []
def Fib1(N):
    if N < len(fib):
        #print("Fast")
        return fib[N-1]
    if N == 1 or N == 2:
        if N > len(fib):
            fib.append(1)
        return 1
    #print("Slow")
    y = Fib1(N-2) + Fib1(N-1)
    if N > len(fib):
        fib.append(y)
    return y
I = random.randint(1,40)
#N = 4181
print("I = ",I)
N = Fib1(I)
print("Fibonacci Number (N): ", N)
F1 = F2 = 1
#print(1,":",F1)
#print(2,":",F2)
i = 2
while F2 < N:
    F0, F1, F2 = F1, F2, F1+F2
    i += 1
    #print(i,":",F2)
print()
print(i,":",F2)