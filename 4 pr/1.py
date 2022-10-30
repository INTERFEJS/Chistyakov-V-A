# -- coding: utf-8 --
A = int(input("Введите A: "))
B = int(input("Введите B (больше или равно А): "))
C = B + 1
if A <= B:
    for i in range (A, C):
        print(i, end = "; ")
else:
    print("B меньше А")