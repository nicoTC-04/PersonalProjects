from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """respuesta con el click ."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 1500) / 25
        speed.y = (y + 1500) / 25


def inside(xy):
    """Regresas las Esferas cuando una toque el final de la pantalla."""
    return -200 < xy.x < 200 and -1500 < xy.y < 1500


def draw():
    """Dibujar los proyectiles y objetivos."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Movimineto de los proyecticles y los objetivos"""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 7.0
        if not inside(target):
            target.x= 199

    if inside(ball):
        speed.y -= 7.0
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()




