# Красницкий Дмитрий Олегович
# 3 курс ИСИТ ЗФ
# Task Boolean 31

import random
def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a,b,c = [random.randrange(1, 6) for i in range(0,3)]
while not TriangleInequality(a,b,c):
    a,b,c = [random.randrange(1, 6) for i in range(0,3)]
print("Длина a: ", a)
print("Длина b: ", b)
print("Длина c: ", c)
bool_expr = (a == b or a == c or b == c)
print("Треугольник является равнобедренным: ",bool_expr)