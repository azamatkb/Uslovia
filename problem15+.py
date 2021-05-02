a = 17391
b = 546
c = 934
d = a % 17
e = b % 17
f = c % 17
if d < e and d < f:
    print('Остаток меньше всего у ',a)
elif e < f and e < d:
    print('Остаток меньше всего у ',b)
else:
    print('Остаток меньше всего у ',c)
