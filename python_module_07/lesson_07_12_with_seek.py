# Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), яка додає додаткову
# інформацію в файл на шляху path з параметра additional_info,
# і після цього повертає рядок з позиції start_pos довжиною count_chars.



def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, "a") as file:
        file.write(additional_info)
    with open(path, "r") as file:
        text = file.read()
        file.seek(start_pos)
        text2 = file.read(count_chars)
    return text2


# Вимоги:
#
# - функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
# - записувати в кінець файлу рядок additional_info
# - після запису функція має відкрити той самий файл для читання
# - прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
# Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.
