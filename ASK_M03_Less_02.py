def print_params(a = 1, b = 'строка', c = True):
    print('a = ', a, '\tb =', b, '\tc = ', c)


print('\n\t1.Функция с параметрами по умолчанию:')

list_1 = [1, 2, 3, 4, 5]
dictionary_1 = {'1e': True, '2e': False, '3e': True}
print_params()
print_params(list_1)
print_params(False, True, dictionary_1)
print_params(b=25)
print_params(b = 8, c = 13)
print_params(c=[1, 2, 3])
print_params(b = 25)
print_params(c = [1,2,3])

print('\n\t2.Распаковка параметров :')

values_list = [(5, 7, 9, 3), False, 'littlу_string']
values_dict = {'a': True, 'b': 'map_on', 'c': 35.18}
print_params(*values_list)
print_params(**values_dict)

print('\n\t13.Распаковка + отдельные параметры:')

values_list_2 = [False, ('string', 'Enter', False, 89.15)]
print_params(*values_list_2, 42)
