# Користувач вводить число від 0 до 100. Підрахуйте, використовуючи цикл while, 
# суму всіх чисел від першого до введеного числа включно в num. 
# Результат помістити в змінну sum.


num = int(input("Enter the integer (0 to 100): "))
sum = 0
i = 1

while i <= num:
    sum += i
    i += 1

print(sum)
