import pgzrun
TITLE= 'QUIZIZZ'
WIDTH=800
HEIGHT=800
scrollerbox=Rect(0,0,800,100)
questionbox=Rect(20,120,600,150)
answerbox1=Rect(20,290,290,150)
answerbox2=Rect(330,290,290,150)

def draw():
    screen.fill('black')
    screen.draw.filled_rect(scrollerbox,'blue')
    screen.draw.filled_rect(questionbox,'yellow')
    screen.draw.filled_rect(answerbox1,'red')
    screen.draw.filled_rect(answerbox2,'red')
def update():
    pass


pgzrun.go()
