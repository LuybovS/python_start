eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def repeat():
    end = input('\nХотите повторить? Введите "y" или "n"\n')
    while True:
        if end.lower() == 'y':
            return True
        elif end.lower() == 'n':
            return False
        else:
            end = input('\nНе поняли ваш ответ. Введите "y" или "n"\n')
            continue
        
while True:
    
    direction = int(input('Введите 0, если нужно зашифровать данные. Введите 1, если нужно дешифровать.\n'))
    if direction != 0 and direction != 1:
        direction = input('\nНеправильный ответ. Введите 0/1\n')    
    
    language = input('Введите язык алфавита: ru — русский, en — английский\n')
    if language.lower() not in 'ru' and language.lower() not in 'en':
        language = input('\nНеправильный ответ. Введите ru/en\n')
    
    text = input('Введите текст\n')
    
    k = int(input('Введите шаг сдвига\n'))
    
    for i in range(len(text)):
        
        if direction == 0:
            
            if language.lower() == 'ru':
                
                if text[i] in rus_lower_alphabet:
                    x = ord(text[i]) + k
                    if x > 1103:
                        x -= 32
                    print(chr(x), end='')
                    
                elif text[i] in rus_upper_alphabet:
                    x = ord(text[i]) + k
                    if x > 1071:
                        x -= 32
                    print(chr(x), end='')  
                else:
                    print(text[i], end='')                
                    
            if language.lower() == 'en':
                
                if text[i] in eng_lower_alphabet:
                    x = ord(text[i]) + k
                    if x > 122:
                        x -= 26
                    print(chr(x), end='')
                elif text[i] in eng_upper_alphabet:
                    x = ord(text[i]) + k
                    if x > 90:
                        x -= 26
                    print(chr(x), end='')   
                else:
                    print(text[i], end='')
                    
        if direction == 1:
            
            if  language.lower() == 'ru':
                
                if text[i] in rus_lower_alphabet:
                    x = ord(text[i]) - k
                    if x < 1072:
                        x += 32
                    print(chr(x), end='')
                elif text[i] in rus_upper_alphabet:
                    x = ord(text[i]) - k
                    if x < 1040:
                        x += 32
                    print(chr(x), end='')  
                else:
                    print(text[i], end='')
                    
            if language.lower() == 'en':
                
                if text[i] in eng_lower_alphabet:
                    x = ord(text[i]) - k
                    if x < 97:
                        x += 26
                    print(chr(x), end='')
                elif text[i] in eng_upper_alphabet:
                    x = ord(text[i]) - k
                    if x < 65:
                        x += 26
                    print(chr(x), end='')
                else:
                    print(text[i], end='')
                    
    if repeat() == False:
        break
    else:
        continue        