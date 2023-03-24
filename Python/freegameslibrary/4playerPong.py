# importar paquetes
from random import choice, random
from turtle import *
from freegames import vector

# darle valor al azar al aim de la pelota entre (-5, -3) o (3, 5)


def value():
    return (3 + random() * 2) * choice([1, -1])


# valores iniciales de jugadores y pelota
ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0, 3: 0, 4: 0}

# funcion para mover jugador


def move(player, change):
    state[player] += change

# Dibujar rectangulo con  color default negro


def rectangle(x, y, width, height, color="black"):
    up()
    goto(x, y)
    down()
    fillcolor(color)
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

# dibujar juego y mover pelota


def draw():
    clear()
    # rectangulos de los lados
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    # dos rectangulos nuevos arriba y abajo
    rectangle(state[3], -200, 50, 10)
    rectangle(state[4], 190, 50, 10)

    # mover la pelota y cambiar sus valores
    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()

    # condicionales para colisiones de la pelota
    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            # pierde el jugador 1
            rectangle(-200, state[1], 10, 50, "red")
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            # pierde el jugador 2
            rectangle(190, state[2], 10, 50, "red")
            return

    if y < -185:
        low = state[3]
        high = state[3] + 50

        if low <= x <= high:
            aim.y = -aim.y
        else:
            # pierde el jugador 3
            rectangle(state[3], -200, 50, 10, "red")
            return

    if y > 185:
        low = state[4]
        high = state[4] + 50

        if low <= x <= high:
            aim.y = -aim.y
        else:
            # pierde el jugador 4
            rectangle(state[4], 190, 50, 10, "red")
            return

    # modificar la velocidad
    aim.x *= 1.005
    aim.y *= 1.005

    # repetir dependiendo del tiempo
    ontimer(draw, 50)


# main para inicializar las variables y la pantalla
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
onkey(lambda: move(3, -20), 'b')
onkey(lambda: move(3, 20), 'n')
onkey(lambda: move(4, -20), 't')
onkey(lambda: move(4, 20), 'y')
draw()
done()