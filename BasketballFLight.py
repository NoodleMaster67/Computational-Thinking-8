from utils import *
import turtle

screen = turtle.Screen()
screen.tracer(0)

set_background("court")

screen.addshape("flightball.gif")
screen.addshape("FlightDrib.gif")

player = turtle.Turtle()
player.shape("flightball.gif")
player.penup()
player.shapesize(stretch_wid=0.3, stretch_len=0.3)

half_width = screen.window_width() // 2
half_height = screen.window_height() // 2

sprite_width = 20
sprite_height = 20

margin_x = sprite_width // 2
margin_y = sprite_height // 2


def move_up():
    set_moving_sprite()
    new_y = player.ycor() + 20
    if new_y < half_height - margin_y:
        player.sety(new_y)
    screen.update()
    screen.ontimer(reset_sprite, 100)

def move_down():
    set_moving_sprite()
    new_y = player.ycor() - 20
    if new_y > -half_height + margin_y:
        player.sety(new_y)
    screen.update()
    screen.ontimer(reset_sprite, 100)

def move_left():
    set_moving_sprite()
    new_x = player.xcor() - 20
    if new_x > -half_width + margin_x:
        player.setx(new_x)
    screen.update()
    screen.ontimer(reset_sprite, 100)

def move_right():
    set_moving_sprite()
    new_x = player.xcor() + 20
    if new_x < half_width - margin_x:
        player.setx(new_x)
    screen.update()
    screen.ontimer(reset_sprite, 100)

def close_window():
    screen.bye()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(close_window, "Escape")

screen.update()
turtle.mainloop()