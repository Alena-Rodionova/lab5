import sys

y = [23, 34, 89, 88, 20]
r=int(input('введите двухзначное число: ',))
if r>10 and r<100:
    print(y)
    for i in y:
        if int(i)==r:
            print('Вы угадали число! ', r,' есть в списке!')
            t=1
            sys.exit()
        else: t=0
    if t==0:
        print('Увы, такого числа нет')
else: print('Вы ввели неправильное значение')