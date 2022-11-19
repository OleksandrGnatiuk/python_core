def generator_numbers(string=""):
    if len(string) == 0:
        return
    else:
        for w in string.split():
            w = w.strip("$.,")
            if w.isdigit():
                yield int(w)


def sum_profit(string):
    s = 0
    for n in generator_numbers(string):
        s += n
    return s
    


if __name__ == "__main__":
    string = """The resulting profit was: from the southern possessions $ 100, 
    from the northern colonies $500, and the king gave $1000."""
    
    print(sum_profit(string))

# Нехай є рядок з числами (з метою спрощення числа лише цілі), 
# що визначає якісь частини загального доходу. Наприклад,

# "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, 
# and the king gave $1000."

# Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити 
# всі цілі числа в ньому та працювати як генератор, який буде віддавати зазначені 
# числа при зверненні до нього у циклі.

#  З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, 
# коли розбивали на лексеми арифметичний вираз

# Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою 
# yield повертає поточне число.

# Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, 
# та повертає загальну суму прибутку з рядка.