"""
Juego de Pintando
"""
from turtle import *
from freegames import vector

# Función que dibuja la linea
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función que dibuja el cuadrado
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función que dibuja un circulo
def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    dot(abs(end.x-start.x))
 

# Funcion que dibuja un rectangulo
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x-start.x)
        left(90)
        forward(end.y-start.y)
        left(90)
    end_fill()
  
# Funcion que dibuja un triangulo
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

# Función que define cuales son los puntos de inicio y final
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Guarda los valores de las teclas
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# codigo del main
state = {'start': None, 'shape': line}
# setup de la pantalla
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#funciones onkey
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()