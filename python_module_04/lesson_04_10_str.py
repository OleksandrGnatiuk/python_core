# створіть функцію get_random_password, яка буде генерувати випадковий рядок пароля.
#
# Вимоги: у пароля має бути 8 символів.
# для шифрування пароля будемо використовувати наступний набір символів:
# ()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Ці символи лежать у межах від 40 до 126 коду в таблиці ASCII включно, і доступ до них можна отримати за допомогою функції chr.

from random import randint


def get_random_password():
    pw = ''
    for _ in range(8):
        i = randint(40, 126)
        pw += chr(i)
    return pw



if __name__ == "__main__":
    print(get_random_password())



