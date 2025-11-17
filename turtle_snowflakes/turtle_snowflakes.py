import turtle as t
from random import randint

# Настройка экрана и цвета
t.Screen().bgcolor('cyan')
t.speed(0)
t.colormode(255)


def snowflake(size):
    segment = size / 4
    
    t.left(randint(15, 180))  # случайный стартовый угол
    for _ in range(8):  # 8 веток
        for _ in range(3):  # подветки каждой ветки
            t.forward(segment)
            t.left(45)
            t.forward(segment)
            t.backward(segment)
            t.right(90)
            t.forward(segment)
            t.backward(segment)
            t.left(45)
        t.forward(segment)
        
        t.backward(size)
        t.right(45)
    

# Главный цикл рисует столько снежинок, сколько введёт пользователь
for _ in range(int(input())):
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))  # случайный цвет
    t.penup()   
    t.goto(randint(-200, 200), randint(-200, 200))  # случайная позиция
    t.pendown()
    snowflake(randint(10, 90))  # случайный размер
