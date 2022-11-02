# Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії,
# get_grade приймає ключ у вигляді оцінки ECTS, і повертає відповідну п'ятибальну оцінку (перший стовпчик таблиці).
# Друга get_description теж приймає ключ у вигляді оцінки ECTS, але повертатиме пояснення оцінки в текстовому
# форматі (останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента.
# На відсутній ключ функції повинні повертати значення None.

marks = {
    "F": [1, '0-34', 'Unsatisfactorily'],
    "FX": [2, '35-59', 'Unsatisfactorily'],
    "E": [3, '60-66', 'Enough'],
    "D": [3, '67-74', 'Satisfactorily'],
    "C": [4, '75-89', 'Good'],
    "B": [5, '90-95', 'Very good'],
    "A": [5, '96-100', 'Perfectly']
}


def get_grade(key):
    global marks
    result = marks.get(key)
    return result[0] if result else None


def get_description(key):
    result = marks.get(key)
    return result[-1] if result else None


if __name__ == "__main__":
    print(get_grade("A"))
    print(get_description("A"))
