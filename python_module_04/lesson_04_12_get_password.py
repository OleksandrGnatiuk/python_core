# напишіть функцію get_password, яка згенерує нам випадковий надійний пароль та поверне його.
# Алгоритм простий — ми генеруємо пароль за допомогою функції get_random_password і,
# якщо він проходить перевірку на надійність функцією is_valid_password, повертаємо його, якщо ні — повторюємо ітерацію знову.
#
# Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не отримати нескінченний цикл.

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    count = 1
    while count <= 100:
        pw = get_random_password()
        if is_valid_password(pw):
            break
        count += 1
    return pw



if __name__ == "__main__":
    print(get_password())

