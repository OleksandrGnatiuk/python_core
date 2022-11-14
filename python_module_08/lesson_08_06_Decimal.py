# Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне
# типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    number_list = list(map(Decimal, number_list))
    return Decimal(sum(number_list) / len(number_list))


if __name__ == "__main__":
    print(decimal_average([31, 55, 177, 2300, 1.57], 9))




# Увага
# Не забувайте приводити всі числа у списку до типу `decimal`
#
# Приклад:
#
# виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
# виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400