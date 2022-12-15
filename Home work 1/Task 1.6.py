"""
Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""
try:
    revenue = float(input("Введите значение выручки: "))
    costs = abs(float(input("Введите значение издержек: ")))
    profit = revenue-costs
    profitability = profit / revenue
    if profit>0:
        print()
        personnel = int(input(f'Прибыль: {profit}\nВведите численность сотрудников: '))
        profit_per_employee = profit / personnel
        print(f'Прибыль на сотрудника: {profit_per_employee}')
    elif profit<0:
        print(f'Убыток: {profit}')
    else:
        print("В ноль")
except ValueError:
    print("Некорректный ввод. Повторите.")

