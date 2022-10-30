"""
Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, 
приймаючи від користувача операнди (числа) та оператор (детальні умови задачі під кодом).
"""

operand = None
operator = None
wait_for_number = True

while wait_for_number:
    try:
        result = float(input('Введіть числове значення: '))
        wait_for_number = False
    except ValueError:
        print("Потрібно ввести числове значення! Введіть ще раз: ")

while True:
    if not wait_for_number:
        operator = input('Введіть знак математичної дії (+, -, *, /, або "=" ): ')
        if operator == "=":
            print(f"Результат: {result}")
            break
        while operator not in ('+', '-', '*', '/'):
            operator = input('Введіть знак математичної дії (+, -, *, /, або "=" ): ')
        wait_for_number = True
    
    while wait_for_number:
        try:
            operand = float(input('Введіть числове значення: '))
            wait_for_number = False
        except ValueError:
            print("Потрібно ввести числове значення! Введіть ще раз: ")
    if operator == '+':
        result += operand
    elif operator == '-':
        result -= operand
    elif operator == '*':
        result *= operand
    elif operator == '/':
        try:
            result /= operand
        except ZeroDivisionError:
            print("Ділити на нуль не можна! Виконайте іншу дію.")

"""
Умови для цієї задачі:
    Додаток працює з цілими та дійсними числами.
    Додаток вміє виконувати такі математичні операції:
        ДОДАВАННЯ (+)
        ВІДНІМАННЯ(-)
        МНОЖЕННЯ (*)
        ДІЛЕННЯ (/)
    Програма приймає один операнд або один оператор за один цикл запит-відповідь.
    Всі операції програма виконує в порядку надходження — одну за одною.
    Програма виводить результат обчислень, коли отримує від користувача символ =.
    Додаток закінчує роботу після того, як виведе результат обчислення.
    Користувач по черзі вводить числа та оператори.
    Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
    Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
    Додаток коректно опрацьовує ситуацію некоректного введення (exception).

Початкові змінні:

result = None
operand = None
operator = None
wait_for_number = True

result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число operator — рядковий параметр, може містити чотири значення, "+", "-", "*", "/" wait_for_number — прапорець, який вказує, що очікують на вводі оператор (operator) або операнд (operand)


"""