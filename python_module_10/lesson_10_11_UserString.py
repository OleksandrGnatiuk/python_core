from collections import UserString


class NumberString(UserString):

    def number_count(self):
        cnt = 0
        for ch in self.data:
            if ch.isdigit():
                cnt += 1
        return cnt


# Створіть клас NumberString, 
# успадкуйте його від класу UserString, 
# визначте для нього метод number_count(self), 
# який буде рахувати кількість цифр у рядку.