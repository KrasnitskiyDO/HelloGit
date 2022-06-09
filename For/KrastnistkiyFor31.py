# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task For 31

for N in range(1,22,5):
    print("N = ",N)
    A0 = 2
    for k in range(1,N+1):
        A1 = 2 + 1/A0
        print(k," : ",A1)
        A0 = A1