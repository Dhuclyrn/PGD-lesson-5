
import pgzrun
import random

HEIGHT = 450
WIDTH = 500
TITLE = "pizza catcher"

score = 0
gameover = False

# player
player = Actor("pizza")
player.pos = 250, 400

# pizza
pizza = Actor("thing")
pizza.pos = random.randint(30, 470), 50


def draw():
    screen.blit("images (16)", (0, 0))
    player.draw()
    pizza.draw()

    screen.draw.text(
        "Score: " + str(score),
        color="white",
        topleft=(10, 10),
        fontsize=35
    )

    if gameover:
        screen.fill("black")
        screen.draw.text(
            "TIME'S UP!",
            color="yellow",
            center=(WIDTH / 2, 170),
            fontsize=50
        )
        screen.draw.text(
            "You caught {} pizzas!".format(score),
            color="white",
            center=(WIDTH / 2, 240),
            fontsize=35
        )
        screen.draw.text(
            "Restart the game to play again!",
            color="white",
            center=(WIDTH / 2, 300),
            fontsize=20
        )


def move_pizza():
    pizza.x = random.randint(30, WIDTH - 30)
    pizza.y = -30


def update():
    global score

    if gameover:
        return

    # move the player
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # keep player inside the screen
    player.x = max(20, min(WIDTH - 20, player.x))
    player.y = max(20, min(HEIGHT - 20, player.y))

    # make pizza fall
    pizza.y += 4

    # catch pizza
    if player.colliderect(pizza):
        score += 1
        move_pizza()

    # pizza missed
    if pizza.y > HEIGHT + 20:
        move_pizza()


def timer():
    global gameover
    gameover = True


clock.schedule(timer, 60.0)

pgzrun.go()
