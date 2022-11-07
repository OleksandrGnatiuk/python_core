def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    idx = riddle.find(start_letter)
    if idx != -1 and idx + int(word_length) <= len(riddle):
        return riddle[idx:idx + word_length]
    else:
        return ""


if __name__ == "__main__":
    print(solve_riddle("ddfhellokmjh", 5, "h"))



# Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

# Параметри функції:

#     riddle - рядок із зашифрованим словом.
#     word_length – довжина зашифрованого слова.
#     start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
#     reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.

# Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
