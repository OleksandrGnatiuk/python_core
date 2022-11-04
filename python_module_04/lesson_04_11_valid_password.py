# Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

def is_valid_password(password):
    check_len = len(password) == 8
    have_low_letter = False
    have_upper_letter = False
    have_digit = False
    for i in password:
        if i.isalpha and i.islower():
            have_low_letter = True
        if i.isalpha and i.isupper():
            have_upper_letter = True
        if i.isdigit():
            have_digit = True
    return True if check_len and have_low_letter and have_upper_letter and have_digit else False


if __name__ == "__main__":
    print(is_valid_password("hgL1d2dR"))
    print(is_valid_password("5541GH"))



# Критерії надійного пароля:
#
# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.
# Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.