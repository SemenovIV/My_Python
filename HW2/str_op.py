# str_op.py
s = "У лукоморья 123 дуб зеленый 456"
if s.find('я') == -1:
        print ("1) Буквы 'я' нет")
else: 
    print (s.find('я'))
print (s.count('у'))
if s.isalpha == False:
    print (s.upper())
if len(s)>4:
    print(s.lower())
print ('О'+ s[1:])