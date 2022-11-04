# Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику.
# Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти.

def lookup_key(data, value):
    list_keys = []
    for key, val in data.items():
        if val == value:
            list_keys.append(key)
    return list_keys


if __name__ == "__main__":
    data = {"Python": 1991, "Java": 1995, "JS": 1995}
    value = 1995
    print(lookup_key(data, value))

