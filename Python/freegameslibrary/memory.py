from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
tiles = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q"] * 4
state = {'mark': None}
hide = [True] * 64
sum = 0

# Crear cuadrado blanco con bordes negros
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Convertir coordenadas a recuadros
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Convertir recuadros a coordenadas
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Actualizar si el número dentro de los recuadros está oculto o no, después de hacerle click
def tap(x, y):
    global sum
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    sum = sum + 1    
    print(sum)

# Colocar imagen y recuadros encima
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    checa = 0

    while hide[checa] == False:
        checa = checa + 1
        if checa == 64:
            print("GAME OVER")

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+14, y)
        lechuga = randint(0,1)
        if lechuga == 1:
            color('black')
        else:
            color('red')
        write(tiles[mark], font=('Calibri', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()