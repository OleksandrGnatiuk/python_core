import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as file:
        result = {}
        result["contacts"] = contacts
        json.dump(result, file)


def read_contacts_from_file(filename):
    with open(filename, "r") as file:
        result = json.load(file)
        return result["contacts"]


if __name__ == "__main__":
    filename = r"C:\Users\Rezerv\Desktop\data.json"
    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Alisa Porter",
            "email": "alisa2015@gmail.com",
            "phone": "(067) 111-11-11",
            "favorite": True,
        }]
    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))


"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та 
властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json 
та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, 
contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.

Структура json файлу має бути такою:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}
Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, 
збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.
"""