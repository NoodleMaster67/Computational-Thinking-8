import turtle
import time
import random
import math

# SCREEN
wn = turtle.Screen()
wn.setup(900, 600)
wn.bgcolor("darkgreen")
wn.title("Arcade Basketball")

wn.tracer(0)

# GAME STATE
score = 0
ball_shot = False
shot_power = 0
in_shot_zone = False

# COURT
court = turtle.Turtle()
court.hideturtle()
court.penup()
court.color("white")

def draw_court():
    court.clear()

    # court outline
    court.goto(-450, 250)
    court.pendown()
    court.goto(450, 250)
    court.goto(450, -250)
    court.goto(-450, -250)
    court.goto(-450, 250)
    court.penup()

    # hoops
    court.goto(-400, 0)
    court.dot(20)

    court.goto(400, 0)
    court.dot(20)

# TEXT
ui = turtle.Turtle()
ui.hideturtle()
ui.penup()

def draw_ui(msg=""):
    ui.clear()
    ui.goto(0, 260)
    ui.write(f"BASKETBALL | SCORE: {score}", align="center", font=("Arial", 16, "bold"))

    ui.goto(0, 230)
    ui.write(msg, align="center", font=("Arial", 12, "bold"))

# PLAYER
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, -100)

# DEFENDER
cpu = turtle.Turtle()
cpu.shape("square")
cpu.color("red")
cpu.penup()
cpu.goto(100, -100)

# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.hideturtle()

ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0

# RESET SHOT
def reset_shot():
    global ball_shot, shot_power, ball_dx, ball_dy

    ball_shot = False
    shot_power = 0

    ball.hideturtle()
    ball.goto(player.pos())

    draw_ui("MOVE + SPACE TO SHOOT")

# MOVE PLAYER
speed = 10

def up(): player.sety(player.ycor() + speed)
def down(): player.sety(player.ycor() - speed)
def left(): player.setx(player.xcor() - speed)
def right(): player.setx(player.xcor() + speed)

# SHOOT (POWER SYSTEM)
def shoot():
    global ball_shot, shot_power, ball_dx, ball_dy, in_shot_zone

    if ball_shot:
        return

    ball_shot = True
    ball.showturtle()

    # distance to hoop affects accuracy
    distance = abs(player.xcor() - 400)

    in_shot_zone = distance < 120

    # power = random + timing + distance
    base_power = random.randint(6, 10)

    if in_shot_zone:
        accuracy = 1.2
    else:
        accuracy = 0.7

    shot_power = base_power * accuracy

    ball.goto(player.pos())

    ball_dx = shot_power
    ball_dy = random.uniform(1.5, 3)

# KEYBINDS
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(shoot, "space")

# START
draw_court()
draw_ui("MOVE + SPACE TO SHOOT")

reset_shot()

# GAME LOOP
while True:
    wn.update()
    draw_court()

    # CPU DEFENSE (tracks player)
    cpu.setx(cpu.xcor() + (player.xcor() - cpu.xcor()) * 0.05)
    cpu.sety(cpu.ycor() + (player.ycor() - cpu.ycor()) * 0.05)

    # BALL MOVEMENT
    if ball_shot:
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        # gravity
        ball_dy -= 0.15

        # LEFT HOOP (SCORE ZONE)
        if ball.distance(-400, 0) < 25:
            score += 2
            draw_ui("SCORED! 🏀🔥")
            time.sleep(1)
            reset_shot()

        # MISS
        elif ball.ycor() < -250 or ball.xcor() > 450:
            draw_ui("MISS ❌")
            time.sleep(1)
            reset_shot()

    time.sleep(0.02)