# end_count_sum.py
result = 0

while True:
    num = input("Введите число или Стоп для выхода: ")
    if num.upper() == 'СТОП':
        break
    else:
        if num.isdigit():
            result += int(num)
        else:
            print("Ошибка ввода.")
        
print("Сумма:", result)
