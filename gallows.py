from random import *

word_list = ['программирование', 'код', 'переменная', 'функция', 'цикл', 'условие', 'класс', 'объект', 'модуль', 'библиотека', 'синтаксис', 'отладка', 'тестирование', 'алгоритм', 'структура', 'перегрузка', 'инкапсуляция', 'наследование', 'полиморфизм', 'интерфейс']



def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
    ]
    return stages[tries]

def play(word):
    
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6
     
    print('Давайте играть в угадайку слов!')
    
    
    while tries > 0:
        
        print(display_hangman(tries))
        
        print(word_completion)        
        
        coincidences_num = 0
        
        s = input('\nВведите букву или слово целиком\n')
        
        if s.isalpha() == False:
            print('\nВы ввели неправильное значение')
            continue
        
        if len(s) == 1:
            
            guessable_letter = s.upper()
            
            if guessable_letter in guessed_letters:
                print('\nВы уже вводили такую букву, повторите попытку')
                continue            
            else:
                guessed_letters.append(guessable_letter)
                
                for i in range(len(word)):
                    
                    if guessable_letter in word[i]:
                        word_completion = word_completion[0:i] + guessable_letter + word_completion[i + 1:]
                        coincidences_num += 1
                
                if coincidences_num > 0:
                    print('\nПоздравляем, вы отгадали букву! Так держать!')
                    if word_completion ==  word:
                        print(word_completion)
                        print('\nПоздравляем, вы угадали слово! Вы победили!')
                        guessed = True  
                        break
                else:
                    print('\nК сожалению такой буквы нет :(')
                    tries -= 1
                    continue
                        
                
                    
        else:
            
            guessable_word = s.upper()
            
            if guessable_word in guessed_words:
                print('Вы уже вводили это слово, повторите попытку')
                continue        
            else:
                guessed_words.append(guessable_word)        
                if guessable_word ==  word:
                    print(word_completion)
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    guessed = False
                    break
                else: 
                    print('К сожалению слово неправильное')
                    tries -= 1
                
                    
    if guessed == False:
        print(f'Загаданное слово: {word}')
        
def repeat():
    end = input('\nХотите повторить игру? Введите "y" или "n"\n')
    while True:
        if end.lower() == 'y':
            return True
        elif end.lower() == 'n':
            return False
        else:
            end = input('\nНе поняли ваш ответ. Введите "y" или "n"\n')
            continue


while True:
    word = get_word()
    play(word.upper())
    if repeat() == False:
        print('Спасибо за игру!')
        break
    
    