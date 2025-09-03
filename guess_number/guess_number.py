from random import randint


# Проверка корректности введённого числа
def is_valid_number(user_input, max_value):
    return user_input.isdigit() and 1 <= int(user_input) <= max_value


# Запрос у пользователя диапазона
def is_valid_quantity():
    while True:
        quantity = input("Из скольки чисел будем угадывать? ")
        if not quantity.isdigit() or int(quantity) < 1:
            print("Введите положительное целое число!")
            continue
        return int(quantity)


# Основная функция угадывания числа
def checking_number():
    quantity = is_valid_quantity()
    num = randint(1, quantity) # загадываем число
    count = 0 # счётчик попыток
    print('Введите число')

    while True:
        user_num = input()

        # проверяем корректность ввода
        if not is_valid_number(user_num, quantity):
            print(f"А может быть все-таки введем целое число от 1 до {quantity}?")
            continue

        count += 1 # увеличиваем счётчик попыток
        user_num = int(user_num)

        # сравнение с загаданным числом
        if user_num < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif user_num > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print(f'Вы угадали c {count} попытки, поздравляем!')
            break


# Цикл игры
def play():
    print('Добро пожаловать в числовую угадайку')
    while True:
        checking_number()
        user_response = input("Сыграем еще раз?")
        if user_response.lower() != 'да':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


# Запуск программы
play()
