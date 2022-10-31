N = int(input("В какую степень возводить: "))
i = 1
ch = vt = int(input("Какое число возводить: "))
sm = 0
while i != N:
    sm = ch * vt
    ch = sm
    i += 1
print(sm)