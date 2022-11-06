import re


def find_all_words(text, word):
    result = re.findall(word, text, flags=re.IGNORECASE)
    return result

if __name__ == "__main__":
    text = "I bought 77 nuts for 6$ and 110 bolts for 3$."
    word = "for"

    print(find_all_words(text, word))





# Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті.
# Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання,
# тобто, наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. головне,
# щоб зберігався порядок слів, регістр не має значення.
#
# Підказка: функції модуля re приймають ще ключовий параметр flags і ми можемо визначити нечутливість до регістру,
# надавши йому значення re.IGNORECASE