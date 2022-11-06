# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

def real_len(text):
    new_text = text.replace('\n', '').replace('\f', '').replace('\r', '').replace('\t', '').replace('\v', '')
    return len(new_text)



# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#
# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'