'''import pgzrun
import random

WIDTH=600
HEIGHT=600
total_sat=10
satelite=[]
for i in range(10):
    sat=Actor('satelite')
    sat.pos=random.randint(50,550),random.randint(50,550)
    satelite.append(sat)
def draw():
    screen.blit('space',(0,0))
    for i in satelite:
        i.draw()
        num+=1
        screen.draw.text(str(num),red)
        num+=1

def update():
    pass
pgzrun.go()'''

import pgzrun
import random
from time import time
WIDTH = 600
HEIGHT = 600
total_sat = 10
satelite = []
sat_check=0
lines=[]
game_over=False
start_time=time()
for i in range(10):
    sat = Actor('satelite')
    sat.pos = random.randint(50, 550), random.randint(50, 550)
    satelite.append(sat)

def draw():
    global displaytime
    screen.blit('space', (0, 0))
    num = 0
    for sat in satelite:
        sat.draw()
        num += 1
        screen.draw.text(str(num), (sat.x, sat.y - 20), color="white")
    for i in lines:
        screen.draw.line(i[0],i[1],'white')
    if sat_check<10:
        displaytime=time()-start_time
        screen.draw.text(str(round(displaytime)),(10,580),color='white')
    else:
        screen.draw.text(str(round(displaytime)),(10,580),color='white')
    if game_over:
        screen.blit('space', (0, 0))
        screen.draw.text('Game over',(100,100),color='red')

def update():
    pass
def on_mouse_down(pos):
    global sat_check, lines
    if sat_check<10:
        if satelite[sat_check].collidepoint(pos):
            if sat_check:
                lines.append((satelite[sat_check-1].pos,satelite[sat_check].pos))
            sat_check+=1

        else:
            lines=[]
            sat_check=0 

def finish():
    global game_over
    game_over=True
clock.schedule(finish, 15)
pgzrun.go()