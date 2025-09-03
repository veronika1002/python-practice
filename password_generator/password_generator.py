from random import choice


# Функция проверки корректности введенного числа
# Принимает строку и возвращает положительное целое число
def checking_number(num):
    while True:
        if num.isdigit() and int(num) > 0:
            return int(num)
        else:
            num = input('Ошибка: Введенные данные некорректны. Введите число больше нуля! ')


# Функция проверки корректности ответа пользователя (да/нет)
# Возвращает True для 'да', False для 'нет'
def checking_response(response):
    while True:
        if response.lower() == 'да':
            return True
        elif response.lower() == 'нет':
            return False
        else:
            response = input('Ошибка: Введенные данные некорректны. Введите "да" или "нет"! ')


# Функция создания набора символов для генерации пароля
# Спрашивает у пользователя, какие символы включить и исключить
def build_charset():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''

    # Спрашиваем пользователя, какие символы включить
    included_numbers = checking_response(input('Включать ли цифры 0123456789? (да/нет) '))
    included_uppercase_let = checking_response(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет) '))
    included_lowercase_let = checking_response(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) '))
    included_chars = checking_response(input('Включать ли символы !#$%&*+-=?@^_ ? (да/нет) '))
    excluded_chars = checking_response(input('Исключать ли неоднозначные символы il1Lo0O? (да/нет) '))

    # Добавляем выбранные символы
    if included_numbers:
        chars += digits
    if included_uppercase_let:
        chars += uppercase_letters
    if included_lowercase_let:
        chars += lowercase_letters
    if included_chars:
        chars += punctuation
    # Исключаем неоднозначные символы
    if excluded_chars:
        for char in 'il1Lo0O':
            chars = chars.replace(char, '')

    return chars


# Функция генерации паролей
def password_generation(quantity, chars):
    passwords = []

    # Если набор символов пустой, сообщаем пользователю
    if not chars:
        print("Невозможно сгенерировать пароль: нет выбранных символов.")
        return []

    password_length = checking_number(input('Какая будет длина пароля? '))

    # Генерация каждого пароля
    for i in range(1, quantity + 1):
        password = ''
        for _ in range(password_length):
            password += choice(chars)
        passwords.append(password)
    
    print()
    return passwords


# Основной цикл программы
def play():
    print('Привет! 👋 Это программа для генерации паролей. Я помогу тебе создать надёжный пароль по твоим параметрам')
    while True:
        # Генерация и вывод паролей
        quantity = checking_number(input('Сколько паролей нужно сгенерировать? '))
        passwords = password_generation(quantity, build_charset())
        print('Сгенерированные пароли:', *passwords, sep='\n')
        print()
        # Спрашиваем, хочет ли пользователь сыграть еще раз
        replay = input('Желаете сгенерировать пароли еще раз? ')
        if not checking_response(replay):
            print('Программа завершена. Благодарим за использование!')
            break


# Запуск программы
play()
