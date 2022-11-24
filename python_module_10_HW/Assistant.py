from collections import UserDict


class AddressBook(UserDict):
    """Class for creating addressbooks"""

    def add_record(self, record):
        self.data[record.name] = record.show_contact()

    def remove_record(self, record):
        self.data.pop(record.name, None)

    def show_records(self):
        return self.data


class Record:
    """Class for creating contacts"""

    def __init__(self, name, phone=None):
        self.name = name
        if phone is None:
            self.phone = []

    def add_phone(self, phone):
        self.phone.append(phone)

    def change_phone(self, phone):
        self.phones = phone

    def delete_phone(self):
        self.phones = []

    def show_contact(self):
        return {"name": self.name, "phone": self.phone}


class Field:
    pass


class Name:
    pass


class Phone:
    pass


# sasha = Record("Sasha")

# sasha.add_phone("0678742845")
# sasha.add_phone("0971111111")
# sasha.change_phone("0665555555")
# sasha.delete_phone()
# print(sasha.show_contact())

# my_book = AddressBook()

# my_book.add_record(sasha)
# print(my_book.show_records())
# my_book.remove_record(sasha)
# my_book.add_record(sasha)
# print(my_book.show_records())
