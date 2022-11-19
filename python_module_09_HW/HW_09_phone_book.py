# телефонну книгу ведемо у вигляді словника:
phone_book = {}


def format_phone_number(func):
    """ Декоратор для приведення номеру телефону до міжнародного стандарту """

    def wrapper(num):
        new_num = func(num)
        if len(new_num) == 12:
            return f"+{new_num}"
        else:
            return f"+38{new_num}"
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
            return "Enter user name"
        except ValueError:
            return "Phone's number is not correct!"
        except IndexError:
            return "Give me name and phone please"
    return wrapper


@input_error
def say_hello(lst):
    return "How can I help you?"


@input_error
def say_goodbye(lst):
    return "Good bye!"


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
        return f"Contact {name.title()} was created/updated"
    else:
        return ""



@input_error
def show_phone(lst):
    """ Функція відображає номер телефону абонента, ім'я якого було в команді 'phone ...'"""
    name = " ".join(lst)
    return phone_book[name.title()]

def help(lst):
    rules = """List of commands:
    1) if you want to add new contact, please write command: add {name} {phone number}
    2) if you want to change contact, please write command: change {name} {phone number}
    3) if you want to see the phone of contact, please write command: phone {name}
    4) if you want to see all contacts, please write command: show all
    5) if you want to say goodbye, please write one of these commands: good bye / close / exit
    6) if you want to say hello, please write command: hello
    """
    return rules

@input_error
def show_all(lst):
    """ Функція виводить всі записи в телефонній книзі при команді 'show all' """
    if len(phone_book) == 0:
        return "Phone book is empty"
    text = ""
    for name, phone in phone_book.items():
        text += f"{name} {phone}\n"
    return text.strip()

# Словник, де ключі - ключові слова в командах, а значення - функції, які при цих командах викликаються
commands = {
    ("add", "change"): set_number,
    "phone": show_phone,
    "show all": show_all,
    "hello": say_hello,
    ("good bye", "close", "exit"): say_goodbye,
    "help": help
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
                print(commands[key](command[1:]))
                

if __name__ == "__main__":
    main()