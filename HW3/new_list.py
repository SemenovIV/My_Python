#new_list.py
from math import sqrt
lst=[2, 4, 9, 16, 25]
lst1=[]
for x in lst:
    lst1.append(sqrt(x))
lst2=list(map((lambda x: sqrt(x)), lst))
lst3=[sqrt(i) for i in lst]  
print(lst1, lst2, lst3)