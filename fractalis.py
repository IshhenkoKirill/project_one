import turtle
import random # модуль необходим для генерации случайных цисел в цикле for
turtle.title('Fractalis v0.1')
f = turtle.Turtle ()
f.speed(0) # максимальная скорость отрисовки
f.hideturtle() # скрываем целеказатель
def start (north_Y, north_X, west_Y, west_X, east_Y, east_X, ran_Y, ran_X): # функция устанавливает якорные точки фрактала
    f.penup()
    f.goto(north_Y, north_X) # точка север
    f.pendown()
    f.dot(1.5) # здесь и далее указан минимальный размер точки == 1.5
    f.penup()
    f.goto(west_Y, west_X) # точка запад
    f.pendown()
    f.dot(1.5)
    f.penup()
    f.goto(east_Y, east_X) # точка восток
    f.pendown()
    f.dot(1.5)
    f.penup()
    f.goto(ran_Y, ran_X) # произвольная точка отсчета
    f.pendown()
    f.dot(1.5)
    for i in range(10000): # объявляем цикл подбрасываний кубика
        cube = random.randrange(1,7) # бросаем 6-гранный кубик
        if cube == 1 or cube == 2:
            f.setheading(f.towards(north_Y, north_X)) # автоматическая ориентация направления черепахи на точку север
            f.penup()
            f.forward(f.distance(north_Y, north_X)/2) # движение по направлению черепахи (расстояние делим на 2)
            f.pendown()
            f.dot(1.5)          
        elif cube == 3 or cube == 4:
            f.setheading(f.towards(west_Y, west_X)) # автоматическая ориентация направления черепахи на точку запад
            f.penup()
            f.forward(f.distance(west_Y, west_X)/2) # движение по направлению черепахи (расстояние делим на 2)
            f.pendown()
            f.dot(1.5)          
        else:
            f.setheading(f.towards(east_Y, east_X)) # автоматическая ориентация направления черепахи на точку восток
            f.penup()
            f.forward(f.distance(east_Y, east_X)/2) # движение по направлению черепахи (расстояние делим на 2)
            f.pendown()
            f.dot(1.5)
start (0, 300, -300, -300, 300, -300, -50, 50) # вызов функции установки якорных точек и построения фрактала
turtle.exitonclick() # по завершению цикла for, целчком мыши окно с фракталом закрывается

