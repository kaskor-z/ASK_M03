
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(value, collection):
    count_calls()
    return value in collection

calls = 0
string = "В чащах Юга Жил-был Цитрус да но фальшивый Аргумент"
tuple_string = string_info(string)
print(f"длины строки: {tuple_string[0]}\n"
      f"строка в верхнем регистре = {tuple_string[1]}\n"
      f"строка в нижнем регистре  = {tuple_string[2]}")
print(f"исходная строка           = {string}")
print("_______________________________________________________")
short_string = string[8:11].upper()
string_word_list = (string.upper()).split()
print(f'*** 1 *** подстрока "{short_string}" входит в состав списка {string_word_list} ?'
      f'---> {is_contains(short_string, string_word_list)}')
string_word_list.remove(short_string)
print(f'*** 2 *** подстрока "{short_string}" входит в состав списка {string_word_list} ?'
      f'---> {is_contains(short_string, string_word_list)}')
print("_______________________________________________________")
string = "Иван Васильевич меняет профессию"
tuple_string = string_info(string)
print(f"длины строки: {tuple_string[0]}\n"
      f"строка в верхнем регистре = {tuple_string[1]}\n"
      f"строка в нижнем регистре  = {tuple_string[2]}")
print(f"исходная строка           = {string}")
print("_______________________________________________________")
print(f'\n====== Функции в модуле вызывались всего {calls} раз, не считая вызовов функции "count_calls()" =========')

