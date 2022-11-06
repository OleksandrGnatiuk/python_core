import re


def replace_spam_words(text, spam_words):
    result = text
    for spam_word in spam_words:
        if spam_word in text:
            replace_word = '*' * len(spam_word)
            result = re.sub(spam_word, replace_word, result, flags=re.IGNORECASE)

    return result


if __name__ == "__main__":
    text = "Яка гидота ваша заливна риба, це справжна отрута"
    spam_words = ["гидота", "отрута"]
    print(replace_spam_words(text, spam_words))



# застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон.
# Наприклад, всі "погані" слова замінюватимемо зірочками.
# Напишіть функцію replace_spam_words, яка приймає рядок (параметр text),
# перевіряє його на вміст заборонених слів зі списку (параметр spam_words),
# та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *,
# причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.