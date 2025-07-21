import pgzrun
WIDTH = 600
HEIGHT = 600
TITLE='Computers'
def draw():
    x=10
    y=25
    w=580
    h=550 
    r=255
    g=0
    b=0
    for i in range(30):

        obj=Rect(x,y,w,h)
        screen.draw.rect(obj,(r,g,b))
        x+=10
        y+=10
        w-=20
        h-=20
        r-=7
        g+=7
        b+=7
def update():
    pass
pgzrun.go()