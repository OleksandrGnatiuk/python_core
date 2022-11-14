from collections import Counter


def get_count_visits_from_ip(ips):
    dict_count_visits = dict(Counter(ips))
    return dict_count_visits


def get_frequent_visit_from_ip(ips):
    dict_count_visits = Counter(ips)
    frequent_visit = dict_count_visits.most_common(1)
    return tuple(*frequent_visit)


if __name__ == "__main__":
    ips = [
        "85.157.172.253",
        "66.157.100.211",
        "73.103.102.111",
        "85.157.172.253"
    ]
    print(get_count_visits_from_ip(ips))
    print(get_frequent_visit_from_ip(ips))


# Є список IP адрес:
#
# IP = [
#     "85.157.172.253",
#     ...
# ]
# Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник,
# де ключ це IP, а значення – кількість входжень у вказаний список.
#
# Приклад:
#
# {
#     '85.157.172.253': 2,
#     ...
# }
# Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.
# Пример:   ('66.50.38.43', 4)