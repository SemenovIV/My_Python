#cinema_price.py
#val1 Фильм
#val2 День
#val3 Время
#val4 Количество билетов
#val5 Цена выбранного билета
#val6 Размер скидки
val1=input("Выберите фильм ('Пятница', 'Чемпионы', 'Пернатая банда'): ")
val2=input("Выберите дату (Сегодня, Завтра): ")
if val1=='Пятница':
    val3=input("Выберите время (сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб): ")
elif val1=='Чемпионы':
    val3=input("Выберите время (сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб): ")
else:
    val3=input("Выберите время (сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб): ")
val4=int(input("Укажите количество билетов: "))
if val1=='Пятница':
    if val3==12:
        val5=250
    elif val3==16:
        val5=350
    else:
        val5=450
elif val1=='Чемпионы':
    if val3==10:
        val5=250
    elif val3==13:
        val5=350
    else:
        val5=350
else:
    if val3==10:
        val5=350
    elif val3==14:
        val5=450
    else:
        val5=450
if val2=='Завтра':
    if val4<20:
        val6=1
    else:
        val6=0.8
else:
    if val4<20:
        val6=0.95
    else:
        val6=0.8
print ("Вы выбрали фильм: ", val1, "День: ", val2, "Время: ", val3, "Количество билетов: ", val4, "Стоимость: ", val4 * val5 * val6, "рублей")
    
        
    

