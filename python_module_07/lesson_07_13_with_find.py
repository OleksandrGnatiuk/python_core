def get_employees_by_profession(path, profession):
    with open(path, "r") as file:
        lst = []
        lst__employees = file.readlines()
        lst__employees = [line.strip() for line in lst__employees if line]

        for employee in lst__employees:
            res = employee.find(profession)
            if res != -1:
                lst.append(employee)
        s = "".join(lst)
        s = s.replace(profession, "")

        return s.strip()




# Є файл зі списком працівників компанії. У кожному рядку файлу записано інформацію лише одного співробітника. Формат запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.
#
# John courier
# Pipe cook
# Створіть функцію get_employees_by_profession(path, profession). Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)
#
# Вимоги:
#
# відкрийте файл за допомогою with для читання
# отримайте рядки з файлу за допомогою методу readlines()
# за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
# об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про переклад рядків '\n' та зайві прогалини, які треба прибрати)
# приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
# поверніть отриманий рядок із файлу