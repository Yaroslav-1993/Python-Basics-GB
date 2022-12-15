"""
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""
test_list = input('Введите элементы списка с разделителем "|": ').split('|')
el_1 = None
el_2 = None
i = 0
cnt = len(test_list)
if cnt % 2 == 1:
    while i < (cnt - 1):
        el_1 = test_list[i]
        el_2 = test_list[i+1]
        test_list[i] = el_2
        test_list[i + 1] = el_1
        i = i + 2
else:
    while i < (cnt):
        el_1 = test_list[i]
        el_2 = test_list[i+1]
        test_list[i] = el_2
        test_list[i + 1] = el_1
        i = i + 2

print(test_list)
