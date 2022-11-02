# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
# ['Robert Stivenson,28', 'Alex Denver,30']

# Це список рядків із прізвищем та віком співробітника, розділеними комами.
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.
# Детальні умови задачі під кодом.


def write_employees_to_file(employee_list, path):
    try:
        file = open(path, "w")
        for department in employee_list:
            for employee in department:
                file.write(f"{employee}\n")
    except FileNotFoundError:
        print("File not found!")
    finally:
        file.close()


if __name__ == "__main__":
    lst = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
    path = r"C:\Users\Rezerv\Desktop\lessons\homework_06\employee.txt"
    write_employees_to_file(lst, path)



# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
# ['Robert Stivenson,28', 'Alex Denver,30']

# Це список рядків із прізвищем та віком співробітника, розділеними комами.
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.
#
# Функція запису в файл write_employees_to_file(employee_list, path), де:
#
# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:
#
# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# """