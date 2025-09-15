import pgzrun
TITLE= 'QUIZIZZ'
WIDTH=800
HEIGHT=800
scrollerbox=Rect(0,0,800,100)
questionbox=Rect(20,120,600,150)
answerbox1=Rect(20,290,290,150)
answerbox2=Rect(330,290,290,150)
answerbox3=Rect(20,470,290,150)
answerbox4=Rect(330,470,290,150)
timerbox=Rect(640,120,130,150)
skipbox=Rect(650,290,120,330)
currentq=0
totalq=0
timer=10
questions=[]
def draw():
    screen.fill('black')
    screen.draw.filled_rect(scrollerbox,'blue')
    screen.draw.filled_rect(questionbox,'yellow')
    screen.draw.filled_rect(answerbox1,'red')
    screen.draw.filled_rect(answerbox2,'red')
    screen.draw.filled_rect(answerbox3,'red')
    screen.draw.filled_rect(answerbox4,'red')
    screen.draw.filled_rect(timerbox,'blue')
    screen.draw.filled_rect(skipbox,'green')
    message=f'Welcome to Quiz Master q:{currentq} of against {totalq}'
    screen.draw.textbox(message,scrollerbox,color='black')
    screen.draw.textbox(str(timer),timerbox,color='white')
    screen.draw.textbox('skip',skipbox,color='black')

def update():

    scrollerbox.x-=2
    if scrollerbox.right<0:
        scrollerbox.x=800
def load_questions():
    global totalq
    with open('questions.txt') as file:
        for i in file:
            questions.append(i)
            totalq+=1

load_questions()
print (questions)
pgzrun.go()
