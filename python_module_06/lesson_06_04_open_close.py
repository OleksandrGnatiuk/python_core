# Реалізуйте функцію add_employee_to_file(record, path),
# яка у файл (параметр path - шлях до файлу) буде додавати співробітника (параметр record)
# у вигляді рядка "Drake Mikelsson,19".

def add_employee_to_file(record, path):
    try:
        file = open(path, "a")
        file.write(f"{record}\n")
    except FileNotFoundError:
        print("File not found!")
    finally:
        file.close()



# Вимоги:
# - параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
# - кожен запис у файл має починатися з нового рядка.
# - необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a', додайте співробітника record у файл і закрийте його
# - ми поки що не використовуємо менеджер контексту with