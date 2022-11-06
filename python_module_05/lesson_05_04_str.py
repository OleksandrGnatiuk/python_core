# Напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name)
# і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname.
# Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.


def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)


if __name__ == "__main__":
    print((is_check_name("Олександр Гнатюк", "Олександр")))


