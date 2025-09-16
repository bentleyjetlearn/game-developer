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
finished=False 
answerboxes=[answerbox1, answerbox2, answerbox3, answerbox4]
score=0
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
    screen.draw.textbox(q[0].strip(),questionbox,color='black')
    screen.draw.textbox(q[1].strip(),answerbox1,color='black')
    screen.draw.textbox(q[2].strip(),answerbox2,color='black')
    screen.draw.textbox(q[3].strip(),answerbox3,color='black')
    screen.draw.textbox(q[4].strip(),answerbox4,color='black')

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
def readq():
    global currentq
    currentq+=1
    return questions.pop(0).split('|')
def updatetime():
    global timer, score
    if timer:
        timer-=1
    else:
        game_over()
def game_over():
    global timer, finished, q
    msg=f'Game over!You scored {score}'
    q=[msg,'-','-','-','-',0]
    timer=0
    finished=True
def on_mouse_down(pos):
    boxnum=1
    for i in answerboxes:
        if i.collidepoint(pos):
                if boxnum is int(q[5]):
                    correct()
                else:
                    game_over()
        boxnum+=1 
    if skipbox.collidepoint(pos):
        skip()

def correct():
    global q, timer, score
    score+=1
    if questions:
        q=readq()
        timer=10
    else:
        game_over()

def skip():
    global timer, q
    if questions:
        q=readq()
        timer=10
    else:
        game_over()



clock.schedule_interval(updatetime,1)
load_questions()
q=readq()
pgzrun.go()
