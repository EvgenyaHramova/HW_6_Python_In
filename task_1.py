# Создайте модуль и напишите в нём функцию, которая получает на вход дату 
# в формате DD.MM.YYYY и возвращает истину, если дата может существовать 
# или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию

def _leap_year(date_int):
    if (date_int[2] % 4 == 0 and date_int[2] % 100 != 0) or date_int[2] % 400 == 0:
        return True

def calendar(date_int):
    if 1 <= date_int[2] <= 9999:
        if date_int[1] in [1, 3, 5, 7, 8, 10, 12] and 1 <= date_int[0] <= 31:
            print('Дата введена корректно')
            return True
        elif date_int[1] in [4, 6, 9, 11] and 1 <= date_int[0] <= 30:
            print('Дата введена корректно')
            return True
        elif (1 <= date_int[0] <= 29) and  _leap_year(date_int):
            print('Дата введена корректно')
            return True
        else:
            print('Дата введена неверно')
            return False
    print('Дата введена неверно')
    return False
    


date = (input('Введите дату в формате DD.MM.YYYY: ').split('.'))
date_int = list(map(int, date))
#print(date_int)
calendar(date_int)


if __name__ == '__main__':
    print('Я не поняла, как это работает и для чего нужно. Сорри.....')