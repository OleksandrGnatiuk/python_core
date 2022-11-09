# Напишіть функцію визначення кількості днів у конкретному місяці. 
# Ваша функція повинна приймати два параметри: month - номер місяця у вигляді 
# цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. 
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.


from datetime import date


def get_days_in_month(month, year):
    if month < 12:
        difference = date(year, month + 1, 1) - date(year, month, 1)
        return difference.days
    else:
        return 31


if __name__ == "__main__":
    print(get_days_in_month(2, 2020))

