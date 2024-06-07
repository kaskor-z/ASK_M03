
def calculation_int(data_structure_int, sum_):      # подсчёт сумма чисел
    sum_ += data_structure_int
    return sum_

def calculation_str(data_structure_str, sum_):      # подсчёт длина строк
    d_s = data_structure_str.replace(' ', '')
    sum_ += len(d_s)
    return sum_

def unpacking_list(data_structure_list, struct):       # распаковка списока
    struct += data_structure_list
    return struct

def unpacking_tuple(data_structure_tuple, struct):      # распаковка кортежа
    struct += list(data_structure_tuple)
    return struct


def unpacking_dict(data_structure_dict, struct):       # распаковка словар
    struct += data_structure_dict.keys()
    struct += data_structure_dict.values()
    return struct


def unpacking_set(data_structure_set, struct):        # расапаковка множества
    struct = list(data_structure_set)
    return struct


def calculate_structure_sum(data_structure):
    sum_ = 0
    struct_1 = []
    while len(data_structure) != 0:
        if type(data_structure[0]) == int:
            sum_ = calculation_int(data_structure[0], sum_)
            data_structure .pop(0)
        # elif type(data_structure[0]) == float:    # В условиях задания нет алгоритма
        #     print(F'sum_ = {sum_}  type = float') #    подстчёта чисел типа float
        elif type(data_structure[0]) == str:
            sum_ = calculation_str(data_structure[0], sum_)
            data_structure .pop(0)
        elif type(data_structure[0]) == list:
            struct_1 = unpacking_list(data_structure[0], struct_1)
            data_structure.pop(0)
        elif type(data_structure[0]) == tuple:
            struct_1 = unpacking_tuple(data_structure[0], struct_1)
            data_structure.pop(0)
        elif type(data_structure[0]) == dict:
            struct_1 = unpacking_dict(data_structure[0], struct_1)
            data_structure.pop(0)
        elif type(data_structure[0]) == set:
            struct_1 = unpacking_set(data_structure[0], struct_1)
            data_structure.pop(0)
    if len(struct_1) != 0:
        #           РЕКУРСИЯ:
        sum_ += calculate_structure_sum(struct_1)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(F'Остаток структуры после итераций = {data_structure};   сумма = {result}')
