import pgzrun
import random
TITLE='ALiengame'
WIDTH=600
HEIGHT=600
alien=Actor('alien')
alien.pos=random.randint(10,580),random.randint(10,580)
message=''
def draw():
    screen.fill('red')
    alien.draw()
    screen.draw.text(message,(400,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message='good shot'
        alien.pos=random.randint(10,580),random.randint(10,580)
    else:
        message='good luck next time'

pgzrun.go()