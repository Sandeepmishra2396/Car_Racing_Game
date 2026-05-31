# ADVANCED CAR RACING GAME - PYTHON TURTLE

import turtle
import random
import time

# SCREEN SETUP

win = turtle.Screen()
win.title("Ultimate Car Racing Game")
win.bgcolor("skyblue")
win.setup(width=1000, height=800)
win.tracer(0)

# DRAW CITY BACKGROUND

drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()
drawer.hideturtle()

# Grasss

drawer.goto(-500, -400)
drawer.color("green")
drawer.begin_fill()

for _ in range(2):
    drawer.forward(1000)
    drawer.left(90)
    drawer.forward(250)
    drawer.left(90)

drawer.end_fill()

# Road
drawer.goto(-150, -400)
drawer.color("gray")
drawer.begin_fill()

for _ in range(2):
    drawer.forward(300)
    drawer.left(90)
    drawer.forward(800)
    drawer.left(90)

drawer.end_fill()

# Road lines
drawer.color("white")

for y in range(-350, 400, 80):
    drawer.goto(0, y)
    drawer.begin_fill()

    for _ in range(2):
        drawer.forward(10)
        drawer.left(90)
        drawer.forward(40)
        drawer.left(90)

    drawer.end_fill()

# TREES

def draw_tree(x, y):

    # trunk
    drawer.goto(x, y)
    drawer.color("brown")
    drawer.begin_fill()

    for _ in range(2):
        drawer.forward(20)
        drawer.left(90)
        drawer.forward(40)
        drawer.left(90)

    drawer.end_fill()

    # leaves
    drawer.goto(x - 20, y + 40)
    drawer.color("darkgreen")
    drawer.begin_fill()
    drawer.circle(40)
    drawer.end_fill()

# Draw many trees
for i in range(-450, -200, 80):
    draw_tree(i, random.randint(-350, 300))

for i in range(200, 450, 80):
    draw_tree(i, random.randint(-350, 300))

# ======================
# HOUSES
# ======================

def draw_house(x, y):

    # body
    drawer.goto(x, y)
    drawer.color("orange")
    drawer.begin_fill()

    for _ in range(4):
        drawer.forward(60)
        drawer.left(90)

    drawer.end_fill()

    # roof
    drawer.goto(x, y + 60)
    drawer.color("red")
    drawer.begin_fill()

    drawer.goto(x + 30, y + 100)
    drawer.goto(x + 60, y + 60)
    drawer.goto(x, y + 60)

    drawer.end_fill()

# Left side houses
for i in range(-470, -250, 100):
    draw_house(i, random.randint(-350, 250))

# Right side houses
for i in range(250, 470, 100):
    draw_house(i, random.randint(-350, 250))

# ======================
# PEOPLE
# ======================

def draw_person(x, y):

    # head
    drawer.goto(x, y)
    drawer.color("peachpuff")
    drawer.begin_fill()
    drawer.circle(10)
    drawer.end_fill()

    # body
    drawer.goto(x + 5, y - 20)
    drawer.color("blue")
    drawer.pendown()
    drawer.goto(x + 5, y - 50)

    # arms
    drawer.goto(x + 5, y - 30)
    drawer.goto(x - 10, y - 40)

    drawer.penup()

# Draw people
for i in range(8):
    draw_person(random.randint(-450, 450), random.randint(-350, 350))

# ======================
# PLAYER CAR
# ======================

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("red")
player.shapesize(stretch_wid=2, stretch_len=1)
player.penup()
player.goto(0, -300)

# ======================
# ENEMY CARS
# ======================

enemies = []

colors = ["yellow", "blue", "white", "black", "purple"]

for i in range(5):

    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("square")
    enemy.color(random.choice(colors))
    enemy.shapesize(stretch_wid=2, stretch_len=1)
    enemy.penup()

    x = random.choice([-80, 0, 80])
    y = random.randint(100, 800)

    enemy.goto(x, y)

    enemies.append(enemy)

# ======================
# SCORE
# ======================

score = 0
high_score = 0
speed = 20

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)

pen.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Arial", 24, "bold")
)

# ======================
# PLAYER MOVEMENT
# ======================

def move_left():

    x = player.xcor()

    if x > -80:
        player.setx(x - 80)

def move_right():

    x = player.xcor()

    if x < 80:
        player.setx(x + 80)

# Keyboard
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# ======================
# GAME LOOP
# ======================

while True:

    win.update()

    for enemy in enemies:

        # Move enemy down
        enemy.sety(enemy.ycor() - speed)

        # Respawn enemy
        if enemy.ycor() < -400:

            enemy.sety(random.randint(400, 800))
            enemy.setx(random.choice([-80, 0, 80]))

            score += 10

            if score > high_score:
                high_score = score

            pen.clear()

            pen.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Arial", 24, "bold")
            )

        # Collision Detection
        if player.distance(enemy) < 30:

            pen.goto(0, 0)

            pen.write(
                "GAME OVER",
                align="center",
                font=("Arial", 40, "bold")
            )

            time.sleep(3)

            # Reset Game
            player.goto(0, -300)

            score = 0

            pen.clear()

            pen.goto(0, 350)

            pen.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Arial", 24, "bold")
            )

            for enemy in enemies:
                enemy.goto(
                    random.choice([-80, 0, 80]),
                    random.randint(100, 800)
                )

    time.sleep(0.03)

win.mainloop()