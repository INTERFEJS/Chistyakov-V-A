# -- coding: utf-8 --
#Вариант-14
def func(N):
    lst = []
    lst.append(N)
    while N != 0:
        N = int(input("Введите число: "))
        if N != 0:
            lst.append(N)
    print(lst.index(max(lst)))
func(int(input("Введите число (чтобы закончить ввод введите 0): ")))