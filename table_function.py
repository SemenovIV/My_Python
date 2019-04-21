# table_function.py
value = input("Введите атомарный номер: ")
if value.isdigit():
    AN = float(value)
    if AN == 3:
        print("Литий")
    elif AN == 25:
        print("Марганец")
    elif AN == 80:
        print("Ртуть")
    elif AN == 17:
        print("Хлор")
    else:
        print("Нет в базе")
else:
    print("Введите атомарный номер!")
