import pgzrun,random
WIDTH = 600
HEIGHT=500
score=0
bee=Actor('bee')
bee.pos=random.randint(10,450),random.randint(10,450)
flower=Actor('flower')
flower.pos=random.randint(10,450),random.randint(10,450)
game_over=False
def draw():
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score),(10,450),fontsize=30)
    if game_over:
        screen.fill('gold') 
        screen.draw.text(f'Game Over.You scored {score}',color='black',center=(250,250),fontsize=30)
def update():
    global score
    if keyboard.left:
        bee.x-=5
    if keyboard.right:
        bee.x+=5
    if keyboard.up:
        bee.y-=5
    if keyboard.down:
        bee.y+=5 
    if bee.colliderect(flower):
        score+=50
        flower.pos=random.randint(10,450),random.randint(10,450)
def finish():
    global game_over
    game_over=True
clock.schedule(finish,15)
pgzrun.go()

