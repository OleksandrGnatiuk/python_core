from functools import reduce


def amount_payment(payment):
    return reduce(lambda x, y: x+y, filter(lambda x: x > 0, payment))
    

if __name__ == "__main__":
    payment = [1, -3, 4]
    print(amount_payment(payment))



# Повернемося до нашого першого завдання з четвертого модуля і перепишемо 
# його за допомогою функції reduce.

# payment = [1, -3, 4]

# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum = sum + value
#     return sum

# Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг 
# наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, 
# чи додатними, якщо необхідно сплатити за рахунками. 
# За допомогою reduce підсумуйте додатні значення та поверніть з функції 
# amount_payment суму платежу в кінці місяця.