def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while len(str_number) -1 == 0:
        return first
    else:
        i = 1
        while str_number[i] == '0':
            i += 1
        return first * get_multiplied_digits(int(str_number[i:]))


number_input = input('\nВведите исходное число =  ') #  исходное число по условиям задания = 40203
result = get_multiplied_digits(int(number_input))
print('**** Произведение цифр в составе числа = ', result)
