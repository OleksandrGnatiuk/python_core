# Напишіть функцію get_phone_numbers_for_сountries, яка буде:
#- Приймати список телефонних номерів.
#- Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
#- Сортувати телефонні номери за вказаними у таблиці країнами.
#- Повертати словник зі списками телефонних номерів для кожної країни
# детальні умови задачі - див. під кодом.


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .replace("+", "")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    country_list_phones = dict()
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.startswith("81"):
            if "JP" in country_list_phones:
                country_list_phones["JP"].append(phone)
            else:
                country_list_phones["JP"] = [phone]

        elif phone.startswith("65"):
            if "SG" in country_list_phones:
                country_list_phones["SG"].append(phone)
            else:
                country_list_phones["SG"] = [phone]

        elif phone.startswith("886"):
            if "TW" in country_list_phones:
                country_list_phones["TW"].append(phone)
            else:
                country_list_phones["TW"] = [phone]

        else:
            if "UA" in country_list_phones:
                country_list_phones["UA"].append(phone)
            else:
                country_list_phones["UA"] = [phone]
    return country_list_phones






# Напишіть функцію get_phone_numbers_for_сountries, яка буде:
#
# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
#
