#game_num.py
from random import randint
val1=randint(1,10)
tr=5
while tr>0:
    val2=input('Введите число от 1 до 10 (или Выход): ')
    if val2 == 'Выход':
        print('Выход из программы.')
        break
    elif int(val2)==val1:
        print('Победа!')
        break
    elif int(val2)>val1:
        print('Ваше число больше')
    else:
        print('Ваше число меньше')
    tr = tr - 1
    print('У вас осталось', tr, 'попыток')
    if tr==0:
        print('У вас закончились попытки. Выход.')