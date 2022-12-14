# У нас є список показників студентів групи – це список з отриманими балами з тестування. 
# Необхідно поділити список на дві частини. Напишіть функцію split_list, 
# яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. 
# У перший потрапляють значення менше середнього, включаючи середнє значення, 
# тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. 
# Для порожнього списку повертаємо два порожні списки.


def split_list(grade):
    low_marks = []
    hight_marks = []

    if len(grade) > 0:
        middle_mark = sum(grade) / len(grade)
        for mark in grade:
            if mark <= middle_mark:
                low_marks.append(mark)
            else:
                hight_marks.append(mark)
    return low_marks, hight_marks


if __name__ == "__main__":
    print(split_list([10, 9, 12, 12, 8, 10, 9, 10, 7, 8]))
