hex_digits = "0123456789ABCDEF"


# Функция проверки корректности введенной системы счисления
def checking_number_system(num_system):
    while True:
        if num_system.isdigit() and int(num_system) in [2, 8, 10, 16]:
            return int(num_system)
        else:
            num_system = input('Введенные данные некорректны. Введите систему счисления: 2, 8, 10 или 16! ')


# Функция проверки корректности введенного числа в выбранной системе
def checking_number(num, base):
    num = num.upper()
    while True:
        for n in num:
            if (
                base == 2 and not n in '01'
                or base == 8 and not n in '01234567'
                or base == 10 and not n in '0123456789'
                or base == 16 and not n in hex_digits
            ):
                num = input('Введенные данные некорректны. Введите число, принадлежащее введенной системе счисления! ')
                break
        else:
            return num


# Функция проверки ответа пользователя (да/нет)
def checking_response(response):
    while True:
        if response.lower() == 'да':
            return True
        elif response.lower() == 'нет':
            return False
        else:
            response = input('Введенные данные некорректны. Введите "да" или "нет"! ')


# Функция перевода числа из десятичной системы в любую другую
# Сделана для практики работы с алгоритмами перевода чисел между системами счисления
def decimal_to_base(num, base):
    base_num = ''
    num = int(num)

    if num == 0:
        return "0"
    
    while num >= base:
        remainder = num % base
        base_num += hex_digits[remainder]
        num //= base

    base_num += hex_digits[num]

    return base_num[::-1]


# Функция перевода числа из любой системы в десятичную
# Сделана для практики работы с алгоритмами перевода чисел между системами счисления
def base_to_decimal(num, base):
    decimal_num = 0
    num = num[::-1]

    for i in range(len(num)):
        letter = num[i]
        decimal_num += (hex_digits.find(letter)) * (base ** i)

    return decimal_num



# Функция перевода числа из одной системы в другую
def number_conversion():
    from_base = checking_number_system(input("Введите систему, из которой переводим: "))
    to_base = checking_number_system(input("Введите систему, в которую переводим: "))
    number_str = checking_number(input("Введите число: "), from_base)

    if from_base == to_base:
        return number_str
    elif from_base == 10:
        return decimal_to_base(number_str, to_base)
    elif to_base == 10:
        return base_to_decimal(number_str, from_base)
    else:
        decimal_num = base_to_decimal(number_str, from_base)
        return decimal_to_base(decimal_num, to_base)


# Основной цикл программы
def play():
    print('Привет! Это Калькулятор систем счисления.')
    while True:
        result = number_conversion()
        print(f'Результат: {result}')
        # Спрашиваем, хочет ли пользователь воспользоваться программой еще раз
        replay = input('Желаете воспользоваться калькулятором еще раз? ')
        if not checking_response(replay):
            print('Программа завершена. Благодарим за использование!')
            break


play()
