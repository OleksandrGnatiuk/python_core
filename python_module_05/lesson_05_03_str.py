# Необхідно реалізувати функцію sanitize_phone_number,
# яка прийматиме рядок з телефонним номером та буде нормалізувати його,
# тобто. буде прибирати символи (, -, ), + та пробіли.




def sanitize_phone_number(phone):
    return phone.strip().replace("(", "").replace(")", "").replace("+", "").replace("-", "").replace(" ", "")


if __name__ == "__main__":
    phone = "    +38(050)123-32-34"
    print(sanitize_phone_number(phone))