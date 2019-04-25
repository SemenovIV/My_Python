import random
val2=random.randint(1, 4)
val1=int(input('Введите число от 1 до 4: '))
if val1==val2:
    print ("Победа!")
elif val1>val2:
    print("Ваше число больше!")
else:
    print("Ваше число меньше!")
