print("Определитель самого большого и самого маленького числа.")
a=int(input('Введите первое число = '))
b=int(input('Введите второе число = '))
c=int(input('Введите третье число = '))
if a > b and a > c:
        print('Максимальное число равно',a)
        if b > c:
                print('Минимальное число равно',c)
        elif b < c:
                print('Минимальное число равно',b)
        else:
                print('Минимальные числа равны', b , ' и ', c ) 
elif b > a and b > c:
        print('Максимальное число равно',b)
        if a > c:
                print('Минимальное число равно',c)
        elif a < c:
                print('Минимальное число равно',a)
        else:
                print('Минимальные числа равны', a , ' и ', c ) 
elif c > a and c > b:
        print('Максимальное число равно',c)
        if a > b:
                print('Минимальное число равно',b)
        elif a < b:
                print('Минимальное число равно',a)
        else:
                print('Минимальные числа равны', a , ' и ', b )
elif a == b and b == c:
        print('Все числа равны')
elif a == b:
        print('Максимальные числа равны', a , ' и ', b )
        print('Минимальное число равно',c)
elif b == c:
        print('Максимальные числа равны', b , ' и ', c )
        print('Минимальное число равно',a)
else:
        print('Максимальные числа равны', a , ' и ', c )
        print('Минимальное число равно',b)
