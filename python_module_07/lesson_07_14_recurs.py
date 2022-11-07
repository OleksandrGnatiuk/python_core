# Напишіть функцію to_indexed(start_file, end_file), яка зчитуватиме вміст файлу, додаватиме до
# прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

def to_indexed(source_file, output_file):
    lst = []
    with open(source_file, "r") as in_file:
        text = in_file.readlines()

        for num, line in enumerate(text):
            s = f"{num}: {line}"
            lst.append(s)
    with open(output_file, "w") as out_file:
        for s in lst:
            out_file.write(f"{s}")



# Напишіть функцію to_indexed(start_file, end_file), яка зчитуватиме вміст файлу, додаватиме до
# прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.
#
# Кожний рядок у створеному файлі повинен починатися з його номера,
# двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

# Нумерація рядків іде від 0.