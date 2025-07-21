import pgzrun
WIDTH = 600
HEIGHT = 600
TITLE = 'Hengstar'
def draw():
    obj=Rect(0,0,600,100)
    obj.center=(300,300)
    screen.draw.filled_rect(obj,'blue')
    screen.draw.circle((300,300),100,'yellow')
    screen.draw.filled_circle((300,300),100,'yellow')
    screen.draw.line((50,75),(500,550),'green')
    screen.draw.text('Hello',(100,125),fontsize=50,color='purple',gcolor='orange',owidth=1.5, ocolor='silver')
def update():
    pass
pgzrun.go()