#count_sum.py
val=input('Введите число')
total=0
for ch in val:
    if int(ch)%2 != 0:
        total += pow(int(ch), 2)
print("Сумма цифр:", total)