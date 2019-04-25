# random_letter1.py
import random
lst=['самовар', 'весна', 'лето']
word=lst[random.randint(0, len(lst)-1)]
indx=random.randint(0, len(word)-1)
letter=word[indx]
print (word[:indx]+'?'+word[(indx+1):])
val=input('Введите пропущенную букву: ')
if val==letter:
    print ('Правильно! Слово: ', word)
else:
    print ('Увы! Попробуйте в другой раз.')