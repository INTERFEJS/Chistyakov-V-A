n = int(input())
m = int(input())
a = []
 
for i in range(n):
    a.append(list(map(int, input().split())))
 
max1 = max(map(max, a))
ind_max1 = a.index(max(a))
ind_max2 = a[ind_max1].index(max1)
 
min1 = min(map(min, a))
ind_min1 = a.index(min(a))
ind_min2 = a[ind_min1].index(min1)
 
a[ind_min1][ind_min2], a[ind_max1][ind_max2] = max1, min1

for i in a:
    print(*i)