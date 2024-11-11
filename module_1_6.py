my_dict = {'Victor': 2003}
print(my_dict)
print(my_dict['Victor'])
print(my_dict.get('Vasily'))
my_dict.update({'Alex': 1991,
                      'Danil': 2007})
print(my_dict)
A = my_dict.pop('Alex')
print(my_dict)
print(A)
my_set = {10, 20, 30, 20, 30, 10, 5, 2, 4, 100, 50, 20}
print(my_set)
my_set.update({1,
               2})
print(my_set)
print(my_set.add(3))
print(my_set)
print(my_set.remove(100))
print(my_set)