# Напишіть рекурсивну функцію encode для кодування списку або рядка.
# Як аргумент функція приймає список (наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ])
# або рядок (наприклад, "XXXZZXXYYYZZ").
# Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).


def encode(data):
    if len(data) == 0:
        return []
    if len(set(data)) == 1:
        return [data[0], len(data)]

    cnt = 1
    i = 1
    while len(data) > 1:
        if data[i] == data[i - 1]:
            cnt += 1
            i += 1
            continue
        return [data[i - 1], cnt] + encode(data[cnt:])


if __name__ == "__main__":
    print(encode("XXXZZXXYYYZZ"))
