from random import *

print('Добро пожаловать в числовую угадайку')
right_limit = int(input('Введите правую границу генирируемого значения: '))
n = randint(1, right_limit)
attempts_number = 0

global end

def is_valid(stroke):
    if stroke.isdigit() == True:
        if 1 <= int(stroke) <= right_limit:
            return True
        else:
            return False
    else:
        return False
    
def replay():
    end = input('\nХотите сыграть еще раз? Введите "Да", если хотите продолжить, и "Нет", если хотите завершить игру.\n')
    while True:
        if end.lower() == 'да':
            attempts_number = 0
            return True
        elif end.lower() == 'нет':
            print('Спасибо за игру!')
            return False
        else:
            end = input('\nМы не поняли ваш ответ, повторите. Введите "Да" если хотите продолжить, и "Нет", если хотите завершить игру.\n')
            continue
    
while True:
    number = input(f'\nВведите число от 1 до {right_limit} включительно: ')
    if is_valid(number) == True:
        number = int(number)
        if number < n:
            print('\nВаше число меньше загаданного, попробуйте еще разок')
            attempts_number += 1
            print('Количество попыток:', attempts_number)
        elif number > n:
            print('\nВаше число больше загаданного, попробуйте еще разок')
            attempts_number += 1
            print('Количество попыток:', attempts_number)
        else:
            print('\nВы угадали, поздравляем!')
            attempts_number += 1
            print('Количество попыток:', attempts_number)
            if replay() == False:
                break
            else:
                right_limit = int(input('Введите правую границу генирируемого значения: '))
        
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue