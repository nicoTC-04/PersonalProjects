"""
Juego de Serpiente
"""
# Importar paquetes
from random import randrange
from turtle import *

from freegames import square, vector

# Coordenada donde empieza la "comida" inicial
food = vector(0, 0)

# Coordenada donde empieza la serpiente
snake = [vector(10, 0)]

# Dirección hacia donde la serpiente se moverá inicialmente
aim = vector(0, -10)

colores = ['blue','yellow','green','purple','black']
colorSerp = colores[randrange(5)]
colorFood = colores[randrange(5)]

# cambiar direccion de la serpiente
def change(x, y):
    aim.x = x
    aim.y = y

# funcion que regresa valor booleano si la serpiente sigue dentro
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# mover la serpiente un lugar
def move():
    head = snake[-1].copy()
    head.move(aim)

    # 1: derecha
    # 2: izquierda
    # 3: arriba
    # 4: abajo

    magic = randrange(1,4)
    if magic==1:
        food.x = food.x + 10
    elif magic==2:
        food.x = food.x - 10
    elif magic==3:
        food.y = food.y + 10
    else:
        food.y = food.y - 10

    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return


    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSerp)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

# Main que instancia todo
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#Funciones onkey
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()