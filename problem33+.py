print ("Определяем отрицательные числа.")
a = int (input ('Введите число: a ='))
b = int (input ('Введите число: b ='))
c = int (input ('Введите число: c ='))
if a < 0 and b < 0 and c < 0:
     print (a, b, c)
elif a < 0 and b < 0 and c > 0:
     print (a, b)
elif a > 0 and b < 0 and c < 0:
     print (b, c)
elif a < 0 and b > 0 and c < 0:
     print (a, c)
elif a < 0 and b > 0 and c > 0:
     print (a)
elif a > 0 and b < 0 and c > 0:
     print (b)
elif a > 0 and b > 0 and c < 0:
     print (c)
else:
        print ("Все числа положительные")
