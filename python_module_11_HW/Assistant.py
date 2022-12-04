from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Name(Field):

    def __str__(self):
        return self.name.title()


class Phone(Field):

    def __init__(self, phone):
        self.__phone = Phone.sanitize_phone_number(phone)

    def __str__(self):
        return self.__phone

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
    @staticmethod
    def sanitize_phone_number(phone):

        new_phone = str(phone).strip().removeprefix("+").replace("(", "").replace(
            ")", "").replace("-", "").replace(" ", "")
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            print("Phone's number is not correct!")
        
        else:
            new_phone = "".join(new_phone)
            return new_phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = Phone.sanitize_phone_number(new_phone)


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

    def __str__(self):
        return self.__birthday.strftime('%Y-%m-%d')

    def __repr__(self):
        return self.__birthday.strftime('%Y-%m-%d')

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, year, month, day):
        self.__birthday = self.validate_date(year, month, day)


class AddressBook(UserDict):
    """Class for creating addressbooks"""

    current_index = 0

    def add_record(self, record):
        self.data[record.name] = record.show_contact()

    def remove_record(self, record):
        self.data.pop(record.name, None)

    def show_records(self):
        return self.data

    def iterator(self):
        for record in self.data.values():
            yield record


class Record:
    """Class for creating contacts"""

    def __init__(self, name, phone=None, birthday: Birthday = None):
        self.name = name
        self.birthday = birthday

        if phone is None:
            self.phone = []
        else:
            self.add_phone = [str(phone)]

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            this_year_birthday = datetime(cur_year, self.birthday.month, self.birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year + 1, self.birthday.month, self.birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"

    def add_birthday(self, year, month, day):
        self.birthday = Birthday.validate_date(year, month, day)
         

    def add_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        self.phone.append(phone)

    def change_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        self.phone = phone

    def delete_phone(self):
        self.phone = []

    def show_contact(self):
        return self.__dict__


sasha = Record("Sasha")
roman = Record("Roman")
sasha_phone = Phone("(067)874-28-45")
# print(sasha_phone)
sasha.add_phone(sasha_phone)
sasha.add_phone("050-11-222-1")
roman.add_phone("0971-110-11")
# sasha.change_phone("0665555555")
# sasha.delete_phone()
# print(sasha.show_contact())

my_book = AddressBook()

my_book.add_record(sasha)
my_book.add_record(roman)

sasha.add_birthday(2016, 3, 7)
# print(sasha.birthday)
# print(my_book.show_records())
# print(sasha.days_to_birthday())
my_book = my_book.iterator()
# print(my_book)
print(next(my_book))
print(next(my_book))