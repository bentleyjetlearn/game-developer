import pgzrun, random
import pygame

WIDTH = 600
HEIGHT = 600
score = 0

boy = Actor('boy')
boy.pos = 300, 300

house = Actor('house')
house.pos = 200, 200

game_over = False

def draw():
    screen.blit('cloudbackg', (0, 0))
    boy.draw()
    house.draw()
    screen.draw.text(str(score), (10, 450), fontsize=30)
    if game_over:
        screen.fill('green')
        screen.draw.text(f'Game Over. You scored {score}', 
                         color='red', center=(250,250), fontsize=30)

def update():
    global score
    if keyboard.left:
        boy.x -= 5
    if keyboard.right:
        boy.x += 5
    if keyboard.up:
        boy.y -= 5
    if keyboard.down:
        boy.y += 5

    if boy.colliderect(house):
        score += 50
        house.pos = random.randint(50, 550), random.randint(50, 550)

def finish():
    global game_over
    game_over = True

clock.schedule(finish, 20)
pgzrun.go()