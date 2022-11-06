# Розробіть функцію sanitize_file(source, output),
# що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.


def sanitize_file(source, output):
    with open(source, 'r') as in_file:
        in_text = in_file.read()
        out_text = ""
        for char in in_text:
            if not char.isdigit():
                out_text += char
    with open(output, 'w') as out_file:
        out_file.write(out_text)




# Вимоги:
#
# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write