'''import pgzrun
import random
from time import time
WIDTH = 600
HEIGHT = 600
total_air = 10
airplane = []
air_check=0
lines=[]
game_over=False
start_time=time()
for i in range(10):
    air = Actor('air')
    air.pos = random.randint(50, 550), random.randint(50, 550)
    air.append(air)

def draw():
    global displaytime
    screen.blit('sky', (0, 0))
    num = 0
    for air in airplane:
        air.draw()
        num += 1
        screen.draw.text(str(num), (air.x, air.y - 20), color="black")
    for i in lines:
        screen.draw.line(i[0],i[1],'black')
    if air_check<10:
        displaytime=time()-start_time
        screen.draw.text(str(round(displaytime)),(10,580),color='black')
    else:
        screen.draw.text(str(round(displaytime)),(10,580),color='black')
    if game_over:
        screen.blit('sky', (0, 0))
        screen.draw.text('Game over',(100,100),color='red')

def update():
    pass
def on_mouse_down(pos):
    global air_check, lines
    if air_check<10:
        if airplane[air_check].collidepoint(pos):
            if air_check:
                lines.append((airplane[air_check-1].pos,airplane[air_check].pos))
            air_check+=1

        else:
            lines=[]
            air_check=0 

def finish():
    global game_over
    game_over=True
clock.schedule(finish, 15)
pgzrun.go()'''

import pgzrun
import random
from time import time

WIDTH = 600
HEIGHT = 600
total_air = 10
airplane = []
air_check = 0
lines = []
game_over = False
start_time = time()

for i in range(10):
    air = Actor('air')
    air.pos = random.randint(50, 550), random.randint(50, 550)
    airplane.append(air)

def draw():
    global displaytime
    screen.blit('sky', (0, 0))
    num = 0
    for air in airplane:
        air.draw()
        num += 1
        screen.draw.text(str(num), (air.x, air.y - 20), color="black")
    for i in lines:
        screen.draw.line(i[0], i[1], 'black')
    if air_check < 10:
        displaytime = time() - start_time
        screen.draw.text(str(round(displaytime)), (10, 580), color='black')
    else:
        screen.draw.text(str(round(displaytime)), (10, 580), color='black')
    if game_over:
        screen.blit('sky', (0, 0))
        screen.draw.text('Game over', (100, 100), color='red')

def update():
    pass

def on_mouse_down(pos):
    global air_check, lines
    if air_check < 10:
        if airplane[air_check].collidepoint(pos):
            if air_check:
                lines.append((airplane[air_check-1].pos, airplane[air_check].pos))
            air_check += 1
        else:
            lines = []
            air_check = 0

def finish():
    global game_over
    game_over = True

clock.schedule(finish, 15)
pgzrun.go()