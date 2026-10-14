import pgzrun
import random

HEIGHT = 450
WIDTH = 500
TITLE = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway, because bees don't care what humans think is impossible."

score = 0
gameover = False

bee=Actor("bee")
bee.pos=100,100

dand=Actor("dand")
dand.pos=200,200

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    dand.draw()
    screen.draw.text("score : "+str(score),color="white",topleft=(10,10))
    if gameover:
        screen.fill("olive") 
        screen.draw.text("Times up you baffon you got {} and\n According to all known laws of aviation,\n there is no way a bee should be able to fly.\n Its wings are too small to get its fat little body off the ground.\n The bee, of course, flies anyway, because bees don't care what humans think is impossible.".format(score),color="white",midtop=(WIDTH/2,10))


def moveflo():
    dand.x = random.randint(50,450)
    dand.y = random.randint(50,450)

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-10
    if keyboard.right:
        bee.x=bee.x+10
    if keyboard.up:
        bee.y=bee.y-10
    if keyboard.down:
        bee.y=bee.y+10
    if bee.colliderect(dand):
        moveflo()
        score += 1 

def timer():
    global gameover
    gameover = True
clock.schedule(timer,10.0)    







pgzrun.go()
