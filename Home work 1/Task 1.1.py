"""
Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните
в переменные, затем выведите на экран.
"""
var_1 =  1
var_2 =  "test"
var_3 =  1.25

print(f'{var_1}, {var_2}, {var_3}')

try:
    var_1 = int(input("Введите целое число: "))
except ValueError:
    var_1 = "Некорректный ввод"
try:
    var_2 = float(input("Введите число с дробной частью: "))
except ValueError:
    var_2 = "Некорректный ввод"
try:
    var_3 = str(input("Введите текстовое значение: "))
except ValueError:
    var_3 = "Некорректный ввод"
print(f'{var_1}, {var_2}, {var_3}')