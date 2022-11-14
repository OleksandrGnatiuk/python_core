import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    a = type(cats)
    if isinstance(cats[0], dict):
        lst = []
        for c in cats:
            d = (c.values())
            a = Cat(*d)
            lst.append(a)
        return lst

    if isinstance(cats[0], Cat):
        lst = []
        for cat in cats:
            lst.append(cat._asdict())

        return lst


if __name__ == "__main__":
    print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
    print(convert_list([{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'},
                        {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]))


# У нас є іменований кортеж для зберігання котів у змінній Cat.
# На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.
#
# Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.
#
# Якщо функція convert_list приймає у параметрі cats список іменованих кортежів
#
# [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# То функція поверне наступний список словників:
#
# [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
# І в той же час, якщо функція convert_list приймає в параметрі cats список словників,
# то результатом буде зворотна операція та функція поверне список іменованих кортежів.
#
# Для визначення типу параметра cats використовуйте функцію isinstance.

