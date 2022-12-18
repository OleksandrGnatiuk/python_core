from collections import UserDict
from datetime import datetime
import pickle
from pathlib import Path


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
            print("Date is not correct\nPlease write 'yyyy-m-d'")
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

    def days_to_bd(self):
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
        self.birthday = Birthday.validate_date(int(year), int(month), int(day))

    def add_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        if phone:
            lst = [phone.phone for phone in self.phones]
            if phone not in lst:
                self.phones.append(Phone(phone))
                return "Phone was added"
        else:
            raise ValueError("Phone number is not correct")

    def change_phone(self, old_phone, new_phone):
        old_phone = Phone.sanitize_phone_number(old_phone)
        new_phone = Phone.sanitize_phone_number(new_phone)

        for phone in self.phones:
            if phone.phone == old_phone:
                phone.phone = new_phone
                return "phone was changed"
        
    def delete_phone(self, phone):
        phone = Phone.sanitize_phone_number(phone)
        for ph in self.phones:
            if ph.phone == phone:
                self.phones.remove(ph)

    def get_contact(self):
        phones = ", ".join([str(p) for p in self.phones])
        return {
            "name": str(self.name),
            "phone": phones,
            "birthday": self.birthday
        }


p = Path("address_book.bin")
address_book = AddressBook()
if p.exists():
    with open("address_book.bin", "rb") as file:
        address_book.data = pickle.load(file)
