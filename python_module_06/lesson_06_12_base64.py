import base64


def encode_data_to_base64(data):
    lst_users = []

    for user in data:
        user = user.encode()
        b64_user = base64.b64encode(user)
        b_user = b64_user.decode()
        lst_users.append(b_user)

    return lst_users


if "__name__" == "__main__":
    data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
    print(encode_data_to_base64(data))


# Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:
#
# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список,
# виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:
#
# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']