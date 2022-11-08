import shutil
from pathlib import Path
import collections
import sys
import random

# створюємо словник, згідно якого визначаємо правила сортування файлів:
suffix_dict = {
    "documents": [".doc", ".docx", ".xls", ".xlsx", ".txt", ".pdf"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "images": [".jpeg", ".png", ".jpg", ".svg"],
    "archives": [".zip", ".gz", ".tar"],
}

# Створюємо функціонал для транслітерації назв на латинські та безпечні символи:
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_", "_")
TRANS = {}
for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def normalize(name):
    """замінюємо кирилічні символи на латинські """
    global TRANS
    return name.translate(TRANS)


def unpack(archive_path, path_to_unpack):
    """ розпаковка архівів"""
    return shutil.unpack_archive(archive_path, path_to_unpack)

def is_file_exists(i, dr):
    """Функція перевіряє, чи вже існує файл з такою назвою.
    Якщо існує, то добавляє до назви в дужках 5 рандомних цифр'"""
    if i in dr.iterdir():
        add_name = ""
        for _ in range(5):
            ch = random.randint(0, 9)
            add_name += str(ch)

        name = i.resolve().stem + f"({add_name})" + i.suffix
        file_path = Path(dr, name)
        return file_path
    return i


def is_fold_exists(i, dr):
    """ Перевіряємо чи існує необхідна папка, якщо немає - створюємо;
    і - посилання на файл, який переміщаємо;    dr - посилання на папку, куди необхідно перемістити файл."""
    if dr.exists():
        folder_sort(i, dr) # передає на функцію, що змінює назву та переміщує файл
    else:
        Path(dr).mkdir()   # створюємо папку з необхідною назвою
        folder_sort(i, dr) # передає на функцію, що змінює назву та переміщує файл


def folder_sort(i, dr):
    """ змінює назву файла та переміщає в необхідну папку.
    і - посилання на файл,  який переміщаємо;    dr - посилання, на папку, куди необхідно перемістити файл."""
    latin_name = normalize(i.name)    # "перекладаємо назву на латинницю"
    new_file = Path(dr, latin_name)   # створюємо шлях до файла з новою назвою
    file_path = is_file_exists(new_file, dr)     # перевіряємо чи вже існує файл з такою назвою
    i.replace(file_path)              # переміщуємо файл



def sort_file(folder, path):
    """ Перевіряє кожну папку та файли по їх розширенню, організовує сортування файлів, та зміну їх назв"""
    p = Path(path)

    for _ in range(2):
        # потрібно два цикла, для видалення пустих папок, що залишаються після рекурсивного обходу, а також для розпаковки архівів.
        for i in p.iterdir():
            if i.name in ("documents", "audio", "video", "images", "archives", "other"): # задаємо перелік папок, для яких сортування вмісту не застосовуємо.
                continue
            if i.is_file():
                # сортування для файлів:
                flag = False  # Якщо флаг не зміниться на True - значить розширення файлу не передбачено правилами. Файл буде відправлено у папку "other"
                for f, suf in suffix_dict.items():
                    if i.suffix.lower() in suf:
                        dr = Path(folder, f)
                        is_fold_exists(i, dr)
                        flag = True  # Якщо розширення файла є в словнику - змінюємо на True
                    else:
                        continue
                if not flag: # Якшо розширення файла немає в словнику (флаг залишається False) ми переміщаємо у "other"
                    dr = Path(folder, "other")
                    is_fold_exists(i, dr)
            elif i.is_dir():
                # операції для папок:
                if len(list(i.iterdir())) != 0:
                    sort_file(folder, i) # якщо папка не пуста - рекурсивно запускаємо в ній функцію
                else:
                    shutil.rmtree(i)  # якщо папка пуста - її удаляємо.

        for j in p.iterdir():
            # в цьому циклі розпаковуємо архіви
            if j.name == "archives" and len(list(j.iterdir())) != 0:
                for arch in j.iterdir():
                    if arch.is_file() and arch.suffix in (".zip", ".gz", ".tar"):
                        arch_dir_name = arch.resolve().stem  # створюємо назву папки, куди розпаковуємо архів (за назвою самого архіва)
                        path_to_unpack = Path(p, "archives", arch_dir_name) # створюємо шлях до папки розпаковки архіва
                        shutil.unpack_archive(arch, path_to_unpack)
                    else:
                        continue


def main():
    try:
        path = sys.argv[1]  # запускаємо через командну строку. Передаємо шлях до папки, в якій необхідно відсортувати файли
        # path = r"/home/oleksandr/Стільниця/trash"
        folder = Path(path)
        p = Path(path)
        sort_file(folder, path)
    except FileNotFoundError:
        print("\nЗаданої папки не знайдено. Перевірте шлях до папки та запустіть команду сортування файлів ще раз\n")


    # Виведення результатів:
    # збираємо статистику сортування файлів у словники
    total_dict = collections.defaultdict(list)  # збираємо всі розширення файлів, що містяться у папці
    files_dict = collections.defaultdict(list)  # збираємо назви всіх файлів, що містяться у папці

    for item in p.iterdir():
        if item.is_dir():
            for file in item.iterdir():
                if file.is_file():
                    total_dict[item.name].append(file.suffix)  # збираємо всі розширення файлів, що містяться у папці
                    files_dict[item.name].append(file.name)    # збираємо назви всіх файлів, що містяться у папці

    for k, v in files_dict.items():
        print()
        print(f" Вміст папки '{k}': ")
        print(f" ---- {v}")

    print()
    print("======================= Сортування файлів успішно завершено! =======================")
    print()
    print("-------------------------------------------------------------------------------------")
    print("| {:^15} | {:^12} | {:^48} |".format("Назва папки ", "к-ть файлів", "розширення файлів"))
    print("-------------------------------------------------------------------------------------")

    for key, value in total_dict.items():
        k, a, b = key, len(value), ", ".join(set(value))
        print("| {:<15} | {:^12} | {:<48} |".format(k, a, b))

    print("-------------------------------------------------------------------------------------")
    print()

if __name__ == "__main__":
    main()