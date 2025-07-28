import random,pgzrun
WIDTH = 600
HEIGHT = 600
TITLE='Computers'
def draw():
    w=550
    h=150
    r=255
    g=random.randint(0,255)
    b=0
    for i in range(20):
        
            obj = Rect(0,0,w,h)
            obj.center=300,300
            screen.draw.rect(obj,(r,g,b))
            w-=20
            h+=20
            r-=10
            b+=10
def update():
    pass
pgzrun.go()
