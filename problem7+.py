print("Собеседование на работу в бюро ритуальных услуг.")
a = str(input('Считаете ли вы себя красивым (Y/N)? - '))
b = str(input('Считаете ли вы себя умным (Y/N)? - '))
c = str(input('Считаете ли вы себя компетентным (Y/N)? - '))

if a == str('y') and b == str('y') and c == str('y'):
        print("Вы нам подходите, мы вас берем!")
elif a == str('n') and b == str('y') and c == str('y'):
        print("Ну красота для нас не главное, мы вас берем!")
elif a == str('y') and b == str('n') and c == str('y'):
        print("Красивые и компетентные люди нам нужны, мы вас берем!")
elif a == str('y') and b == str('y') and c == str('n'):
        print("Ум и красота страшная сила, остальному научим, мы вас берем!")
elif a == str('y') and b == str('n') and c == str('n'):
        print("Красота спасет мир! В нашей работе это полезное качество, мы вас берем!")
elif a == str('n') and b == str('y') and c == str('n'):
        print("Умные люди на вес золота, мы вас берем!")
elif a == str('n') and b == str('n') and c == str('y'):
        print("Опытные люди нам не помешают, мы вас берем!")
else:
        print("Скромность и самокритика признак силы и мудрости! Берем!")
