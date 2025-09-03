ru_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alpha = 'abcdefghijklmnopqrstuvwxyz'


# Функция шифрования/дешифрования текста по Цезарю
def caesar_cipher(text, operation, rotate, alphabet):
    new_text = ''
    for letter in text:
        letter_index = alphabet.find(letter.lower())

        # Если символ не в алфавите, оставляем как есть
        if letter_index == -1:
            new_letter = letter
        # Шифрование
        elif operation == 'шифр':
            new_letter = alphabet[(letter_index + rotate) % len(alphabet)]
        # Дешифрование
        else:
            new_letter = alphabet[(letter_index - rotate) % len(alphabet)]

        # Сохраняем регистр
        if letter.isupper():
            new_letter = new_letter.upper()
            
        new_text += new_letter

    return new_text


# Функция ввода и проверки данных пользователя
def checking_responses():
    # Выбор языка
    user_language = input('На каком языке будем шифровать/дешифровать текст? (рус/англ) ')
    while True:
        if user_language.lower() == 'рус':
            user_language = ru_alpha
            break
        elif user_language.lower() == 'англ':
            user_language = eng_alpha
            break
        else:
            user_language = input('Введенные данные некорректны. Введите "рус" или "англ"! ')

    # Выбор операции
    operation_text = input('Что нужно сделать с текстом, зашифровать или расшифровать? (шифр/дешифр) ')
    while True:
        if operation_text.lower() == 'шифр' or operation_text.lower() == 'дешифр':
            break
        else:
            operation_text = input('Введенные данные некорректны. Введите "шифр" или "дешифр"! ')

    # Ввод сдвига
    shift = input('Какая будет величина сдвига? ')
    while True:
        if shift.isdigit() and int(shift) >= 0 and int(shift) <= len(user_language):
            shift = int(shift)
            break
        else:
            shift = input(f'Ошибка: Введенные данные некорректны. Введите число от 0 до {len(user_language)}! ')

    # Ввод текста и проверка на соответствие выбранному языку
    text = input('Введите текст: ')
    while True:
        for letter in text:
            if letter.isalpha() and letter.lower() not in user_language:
                text = input('Введите текст на том языке, который указали! ')
                break
        else:
            break

    return caesar_cipher(text, operation_text, shift, user_language)


# Основной цикл программы
def play():
    print('Привет! Это программа для шифрования/дешифрования текста. Поехали!')
    while True:
        print(checking_responses())
        print()
        # Спрашиваем, хочет ли пользователь воспользоваться программой еще раз
        replay = input('Желаете попробовать еще раз? ')
        if replay.lower() != 'да':
            print('Спасибо, что воспользовались программой. Еще увидимся...')
            break

play()
