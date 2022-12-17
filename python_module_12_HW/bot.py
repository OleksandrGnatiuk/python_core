from Classes import address_book, Record, AddressBook
import pickle


def say_hello(s):
    return "How can I help you?"


def say_goodbye(s=None):
    return "Good bye!"


def add_contact(value):
    name, *phones = value.lower().strip().split()
    if not name.title() in address_book:
        record = Record(name)
        address_book.add_record(record)
        for phone in phones:
            record.add_phone(phone)
        return f"Contact {name} was created"
    else:
        return f"Contact {name.title()} already exists"


def contact(value):
    """ Функція відображає номер телефону абонента, ім'я якого було в команді 'phone ...'"""
    if value.title() in address_book:
        record = address_book[value.title()]
        return record.get_contact()
    else:
        return f"Contact {value.title()} is not exist"


def help(s):
    rules = """List of commands:
    1) if you want to add new contact, please write command: add {name} {phone number}
    2) if you want to change contact, please write command: change {name} {phone number}
    3) if you want to see the phone of contact, please write command: phone {name}
    4) if you want to see all contacts, please write command: show all
    5) if you want to say goodbye, please write one of these commands: good bye / close / exit
    6) if you want to say hello, please write command: hello
    """
    return rules


def show_all(s):
    """ Функція виводить всі записи в телефонній книзі при команді 'show all' """
    if len(address_book) == 0:
        return "Phone book is empty"
    for contact, record in address_book.items():
        print(record.get_contact())


# Словник, де ключі - ключові слова в командах, а значення - функції, які при цих командах викликаються
commands = {
    "add": add_contact,
    "change": None,
    "phone": contact,
    "show all": show_all,
    "hello": say_hello,
    "good bye": say_goodbye,
    "close": say_goodbye,
    "exit": say_goodbye,
    "help": help
}


def main():
    while True:
        command = input("Enter command: ")

        if command.lower() in (".", "close", "exit", "good bye"):
            say_goodbye()
            break

        for key in commands:
            if command.lower().strip().startswith(key):
                print(commands[key](command[len(key):].strip()))
                break


if __name__ == "__main__":
    main()

    with open("address_book.bin", "wb") as file:
        pickle.dump(address_book.data, file)
