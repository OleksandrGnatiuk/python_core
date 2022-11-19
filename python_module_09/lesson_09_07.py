def normal_name(list_name):
    return list(map(lambda x: x.capitalize(), list_name))
    

if __name__ == "__main__":
    name = ["dan", "jane", "steve", "mike"]

    print(normal_name(name))

# Є список name з іменами користувачів, але всі починаються з малої літери.
# Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, 
# але вже з правильними іменами з великої літери.

# ['Dan', 'Jane', 'Steve', 'Mike']

# Необхідно використовувати функцію map. Не забудьте, 
# що необхідно виконати перетворення типів для map.