# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних 
# у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 
# 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
# Перетворене значення функція повертає під час виклику.


from datetime import datetime


def get_str_date(date):
    dt = date.split()[0]
    d = datetime.strptime(dt, "%Y-%m-%d")
    return datetime.strftime(d, "%A %d %B %Y")
    
    
    
if __name__ == "__main__":
    print(get_str_date('2021-05-27 17:08:34.149Z'))


