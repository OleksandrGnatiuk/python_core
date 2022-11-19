# телефонну книгу ведемо у вигляді словника:
phone_book = {}


def format_phone_number(func):
    """ Декоратор для приведення номеру телефону до міжнародного стандарту
    перевіряє довжину номера """

    def wrapper(num):
        new_num = func(num)
        if len(new_num) == 12:
            return f"+{new_num}"
        elif len(new_num) == 10:
            return f"+38{new_num}"
        else:
            print("Phone's number is too short!")
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (phone.strip().removeprefix("+").replace("(", "")
    .replace(")", "").replace("-", "").replace(" ", ""))
    # перевіряємо чи номер складається тільки з цифр, 
    # якщо номер буде містити інший символ - в декораторі буде відпрацьовано помилку
    new_phone = [str(int(i)) for i in new_phone]
    new_phone = "".join(new_phone)
    return new_phone


def input_error(func):
    """ Декоратор, що повідомляє про виключення """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Phone's number is not correct!")
        except IndexError:
            print("Give me name and phone please")
    return wrapper


@input_error
def say_hello(lst):
    print("How can I help you?")


@input_error
def say_goodbye(lst):
    print("Good bye!")


@input_error
def set_number(lst):
    """Функція записує, або змінює номер в телефонну книгу
    Якщо ім'я складається кількох слів: firstname lastname - об'єднуємо їх в один рядок """
    phone = str(lst[-1])
    name = " ".join(lst[:-1])
    phone = sanitize_phone_number(phone)
    # Запис відбудеться, тільки якщо номер складається лише з цифр та має достатню довжину:
    if phone:
        phone_book[name.title()] = phone


@input_error
def show_phone(lst):
    """ Функція відображає номер телефону абонента, ім'я якого було в команді 'phone ...'"""
    name = " ".join(lst)
    print(phone_book[name.title()])


@input_error
def show_all(lst):
    """ Функція виводить всі записи в телефонній книзі при команді 'show all' """
    if len(phone_book) == 0:
        print("Phone book is empty")
    for name, phone in phone_book.items():
        print(f"{name} {phone}")

# Словник, де ключі - ключові слова в командах, а значення - функції, які при цих командах викликаються
commands = {
    ("add", "change"): set_number,
    "phone": show_phone,
    "show all": show_all,
    "hello": say_hello,
    ("good bye", "close", "exit"): say_goodbye
}

@input_error
def main():
    while True:
        command = input("Enter command: ")
        if command in (".", ):
            break
        command = command.lower().split()
        for key in commands:
            if command[0] in key:
                commands[key](command[1:])
                

if __name__ == "__main__":
    main()