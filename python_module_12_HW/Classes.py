from collections import UserDict
from datetime import datetime
import pickle
import pathlib


class Field:

    def __init__(self, value):
        self.__name = value

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Name(Field):

    @Field.name.setter
    def name(self, value):
        self.__name = value.title()


class Phone(Field):

    def __init__(self, phone):
        self.__phone = phone

    @staticmethod
    def sanitize_phone_number(phone):

        new_phone = str(phone).strip().removeprefix("+").replace(
            "(", "").replace(")", "").replace("-", "").replace(" ", "")
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            print("Phone's number is not correct!")

        else:
            new_phone = "".join(new_phone)
            if len(new_phone) == 12:
                return f"+{new_phone}"
            elif len(new_phone) == 10:
                return f"+38{new_phone}"
            else:
                print("Length of phone's number is wrong")

    def __str__(self):
        return self.__phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = Phone.sanitize_phone_number(phone)


class Birthday(datetime):

    @staticmethod
    def validate_date(year, month, day):
        try:
            birthday = datetime(year=year, month=month, day=day)
        except ValueError:
            print("Date is not correct")
        else:
            return str(birthday.date())

    def __init__(self, year, month, day):
        self.__birthday = self.validate_date(year, month, day)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, year, month, day):
        self.__birthday = self.validate_date(year, month, day)


class AddressBook(UserDict):
    """Class for creating addressbooks"""

    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[str(record.name)] = record

    def remove_record(self, record):
        self.data.pop(str(record.name), None)

    def all_records(self):
        return {key: value.get_contact() for key, value in self.data.items()}

    def iterator(self):
        for record in self.data.values():
            yield record.get_contact()


class Record:
    """Class for creating contacts"""

    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name.title())
        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

        if phone is None:
            self.phones = []
        else:
            self.phones = [Phone(phone)]

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            birthday = datetime.strptime(self.birthday, '%Y-%m-%d')
            this_year_birthday = datetime(cur_year, birthday.month,
                                          birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year + 1, birthday.month,
                                              birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"
        else:
            return f"{self.name}'s birthday is unknown"

    def add_birthday(self, year, month, day):
        self.birthday = Birthday.validate_date(year, month, day)

    def add_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        if phone:
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Перевірте правильніть номера")

    def change_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        self.phones = [Phone(phone)]

    def delete_phone(self):
        self.phone = []

    def get_contact(self):
        phones = ", ".join([str(p) for p in self.phones])
        return {
            "name": str(self.name),
            "phone": phones,
            "birthday": self.birthday
        }


p = pathlib.Path("address_book.bin")
address_book = AddressBook()
if p.exists():
    with open("address_book.bin", "rb") as file:
        address_book.data = pickle.load(file)
"""------------------------------------"""
# sasha = Record("Sasha")
# roman = Record("Roman")
# sasha_phone = Phone("(067)874-28-45")
# print(sasha_phone)
# sasha.add_phone(sasha_phone)
# sasha.add_phone("050-112-1115")

# print(sasha.days_to_birthday())
# print(roman.days_to_birthday())

# roman.add_phone("09712-222-11")
# sasha.delete_phone()
# print(sasha.show_contact())

# address_book.add_record(sasha)
# address_book.add_record(roman)
# roman.change_phone("0665555555")
# sasha.add_birthday(1976, 3, 7)
# roman.add_birthday(2016, 12, 2)
# print(sasha.birthday)
# print(address_book.show_records())
# print(sasha.show_contact())

# print(sasha.days_to_birthday())
# address_book = address_book.iterator()
# print(address_book)
# print(next(address_book))
# print(next(address_book))