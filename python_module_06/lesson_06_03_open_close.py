# створити функцію read_employees_from_file(path),
# яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
#
# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']


def read_employees_from_file(path):
    try:
        file = open(path, "r")
        employees = file.readlines()
        lst = [employee.strip() for employee in employees]
    except FileNotFoundError:
        print("File not found!")
    finally:
        file.close()
    return lst


# ЗАВДАННЯ. ПРОЧИТАТИ ЗАПИСАНИЙ ФАЙЛ
# У попередній задачі ми записали співробітників у файл у такому вигляді:
#
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19

# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path),
# яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
#
# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
#
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу.
# Його необхідно прибирати при додаванні прочитаного рядка до списку.
#
# Вимоги:
# - прочитайте вміст файлу за допомогою режиму "r".
# - ми поки що не використовуємо менеджер контексту with
# - поверніть із функції список співробітників із файлу