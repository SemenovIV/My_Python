#call_tel.py
val1 = int(input("Введите код города: "))
val2 = int(input("Введите длительность разговора: "))
p1=15
p2=18
p3=13
p4=11
if val1 == 343:
    print ("Екатеринбург, ",val2*p1," рублей")
elif val1 == 381:
    print ("Омск, ", val2*p2," рублей")
elif val1 == 473:
    print ("Воронеж, ", val2*p3," рублей")
elif val1 == 485:
    print ("Ярославль, ", val2*p4," рублей")
else:
    print ("Города нет в базе")
