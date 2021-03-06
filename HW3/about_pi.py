# about_pi.py
s = '''В разные эпохи и у разных народов число Пи имело разное значение.
Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело
значение 3.162 китайцы пользовались числом, равным 3.1459
Буквенное обозначение число Пи получило только в 1706 году – оно происходит
от начальных букв двух греческих слов, означающих окружность и периметр.
Буквой π число наделил математик Джонс, а прочно вошла в математику она
уже в 1737 году.'''
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
s1 = [i for i in s.split() if i.isdigit() or is_number(i)==True]

print(', '.join(s1))
print('Количество чисел: ', len(s1))
s2 = [float(i) for i in s1]
print(max(s2))
print(sum(s2))