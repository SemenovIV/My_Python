#del_element_list.py
names=['John', 'Paul', 'George', "Ringo"]
names1=list(filter(lambda x: x=='John'or x=='Paul', names))
print(names1)