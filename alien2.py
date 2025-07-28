import pgzrun
import random
TITLE='ALiengame'
WIDTH=600
HEIGHT=600
alien=Actor('alien')
alien.pos=random.randint(10,580),random.randint(10,580)
message=''
score=0
game_over=False
def draw():
    screen.fill('red')
    alien.draw()
    screen.draw.text(message,(400,10),fontsize=30)
    screen.draw.text(str(score),(10,500),fontsize=30)
    if game_over:
        screen.fill('gold')
        screen.draw.text('You win! Game over!!!',(100,200),fontsize=30)
def update():
    alien.x+=7
    if alien.x>=620:
        alien.x=0
        alien.y=random.randint(10,580) 
def on_mouse_down(pos):
    global message,score,game_over
    if alien.collidepoint(pos):
        message='good shot'
        score+=1
        if score==20:
            game_over=True
        alien.pos=random.randint(10,580),random.randint(10,580)
    else:
        message='good luck next time'

pgzrun.go()