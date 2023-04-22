from random import *

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_.'
ambiguous_characters = 'il1Lo0O'

chars = []
global num
question = ['\nДолжен ли пароль содержать числа? Введите д/н\n',  '\nДолжен ли пароль содержать строчные буквы? Введите д/н\n', '\nДолжен ли пароль содержать прописные буквы буквы? Введите д/н\n', f'\nДолжен ли пароль содержать {punctuation}? Введите д/н\n', f'\nДолжен ли пароль содержать неоднозначные символы {ambiguous_characters}?\n', '\nХотите повторить генерацию паролей? Введите д/н\n']

def challenge_question(q):
    s = input(q)
    if s.lower() == 'д':
        return True
    elif s.lower() == 'н':
        return False
    else:
        s = input('\nНеправильный ответ. Введите д/н\n')
        
def generate_password(l, ch):
    if num < len(ch):
        for i in range(num):
            print(*sample(ch, l), sep='')
    else:
        print ('Нельзя сгенерировать пароль превышающий количество доступных символов')
        
        
while True:
    if challenge_question(question[0]) == True:
        chars.extend(digits)
    if challenge_question(question[1]) == True:
        chars.extend(lowercase_letters)
    if challenge_question(question[2]) == True:
        chars.extend(uppercase_letters)
    if challenge_question(question[3]) == True:
        chars.extend(punctuation)
    if challenge_question(question[4]) == True:
        chars.extend(ambiguous_characters)
        
    num = int(input('\nВведите количество паролей\n'))
    length = int(input('\nВведите длину паролей\n'))
    generate_password(length, chars)
    
    if challenge_question(question[-1]) == False:
        break