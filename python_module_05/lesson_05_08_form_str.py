grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    list_for_print = []
    global grades
    num = 0
    for key, value in students.items():
        num += 1
        list_for_print.append("{:>4}|{:<10}|{:^5}|{:^5}".format(num, key, value, grades[value]))
    return list_for_print





# У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades,
# яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:
#
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# І повертає список відформатованих рядків, щоб під час виведення наступного коду:
#
# for el in formatted_grades(students):
#     print(el)
# Виходила наступна таблиця:
#
#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4
# перший стовпець — ширина 4 символи, вирівнювання по правому краю
# другий стовпець — ширина 10 символів, вирівнювання по лівому краю
# третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
# вертикальний символ | не входить у ширину стовпця