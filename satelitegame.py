import pgzrun
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
def update():
    pass
pgzrun.go()