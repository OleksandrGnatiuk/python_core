from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    """Class for creating 'name' field """

    def __str__(self):
        return self._value.title()


class Phone(Field):
    """Class for creating 'phone' field """

    @staticmethod
    def sanitize_phone_number(phone):
        """Method for change phone number to standart format"""

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

    def __init__(self, value):
        self._value = Phone.sanitize_phone_number(value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.sanitize_phone_number(value)


class Birthday(datetime):
    """Class for creating 'birthday' field"""

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


class Record:
    """Class for creating contacts"""

    def __init__(self,
                 name: Name,
                 phone: Phone = None,
                 birthday: Birthday = None):
        self.name = name
        self.birthday = birthday
        self.phones = []
        if isinstance(phone, Phone):
            self.phones.append(phone)

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            this_year_birthday = datetime(cur_year, self.birthday.month,
                                          self.birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year + 1,
                                              self.birthday.month,
                                              self.birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"

    def add_birthday(self, year, month, day):
        self.birthday = Birthday.validate_date(year, month, day)

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone:
            self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)

        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return "phone was changed"

    def delete_phone(self, old_phone):
        old_phone = Phone(old_phone)
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)

    def get_contact(self):
        phones = ", ".join([str(p) for p in self.phones])
        return {
            "name": str(self.name.value),
            "phone": phones,
            "birthday": self.birthday,
        }


class AddressBook(UserDict):
    """Class for creating addressbooks"""

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        if name in self.data:
            self.data.pop(name)

    def all_records(self):
        return {key: value.get_contact() for key, value in self.data.items()}

    def iterator(self):
        for record in self.data.values():
            yield record.get_contact()


if __name__ == "__main__":

    sasha = Name("Sasha")
    sasha_phone = Phone("(067)874-28-45")
    rec_sasha = Record(sasha, sasha_phone)
    rec_sasha.add_phone("050-112-1222")
    rec_sasha.change_phone("050-112-1222", "095-112-1222")

    roman = Name("Roman")
    roman_phone = Phone("(067)1111111")
    rec_roman = Record(roman, roman_phone)
    rec_roman.add_phone("09712-100-11")
    rec_roman.delete_phone("(067)1111111")

    my_book = AddressBook()
    my_book.add_record(rec_sasha)
    my_book.add_record(rec_roman)

    rec_sasha.add_birthday(2016, 3, 7)
    # print(sasha.birthday)
    # print(my_book.all_records())
    # my_book.remove_record("Sasha")
    print(my_book.all_records())

    # my_book = my_book.iterator()
    # print(next(my_book))
    # print(next(my_book))