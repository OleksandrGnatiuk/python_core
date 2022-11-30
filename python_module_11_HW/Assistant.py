from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return self.phone



    # def format_phone_number(func):
    #     """ Декоратор для приведення номеру телефону до міжнародного стандарту """
        
    #     def wrapper(num):
    #         new_num = func(num)
    #         if len(new_num) == 12:
    #             return f"+{new_num}"
    #         else:
    #             return f"+38{new_num}"
    #     return wrapper

    # @format_phone_number
    @staticmethod
    def sanitize_phone_number(phone):
        new_phone = phone.strip().removeprefix("+").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            return "Phone's number is not correct!"
        else:
            new_phone = "".join(new_phone)
            return new_phone


    # @property
    # def phone(self):
    #     return self.phone

    # @phone.setter
    # def phone(self, new_phone):
    #     self.phone = new_phone


class Birthday(datetime):

    def __init__(self, year, month, day):
        self.birthday = datetime(year=year, month=month, day=day)

    def __str__(self):
        return self.birthday.strftime('%Y-%m-%d')
    
    def __repr__(self):
        return self.birthday.strftime('%Y-%m-%d')



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

    def __init__(self, name, phone=None, birthday: Birthday = None):
        self.name = name
        self.birthday = birthday
        
        if phone is None:
            self.phone = []

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            this_year_birthday = datetime(cur_year, self.birthday.month, self.birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year+1, self.birthday.month, self.birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"

    def add_birthday(self, birthday):
        self.birthday = birthday

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
sasha_phone = Phone("(067)874-28-45")
print(sasha_phone)
sasha.add_phone("(067)874-28-45")
sasha.add_phone("0971-1111-11")
# sasha.change_phone("0665555555")
# sasha.delete_phone()
# print(sasha.birthday)
# print(sasha.show_contact())

my_book = AddressBook()

my_book.add_record(sasha)
# print(my_book.show_records())
# my_book.remove_record(sasha)
# my_book.add_record(sasha)
sasha.add_birthday(Birthday(2016, 3, 7))
# print(sasha.birthday)
print(my_book.show_records())
print(sasha.days_to_birthday())

