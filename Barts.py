from utils import *
import pygame
import sys
import turtle
screen = turtle.Screen()

pygame.init()
player = create_sprite("Fligthshoe", 50, 100)
set_background("highway")
player.shapesize(stretch_wid=0.5, stretch_len=0.5)
player.shapesize(stretch_wid=0.5, stretch_len=0.5)
window.update()

# Screen boundaries
half_width = screen.window_width() // 2
half_height = screen.window_height() // 2

sprite_width = 25
sprite_height = 50

margin_x = sprite_width // 2
margin_y = sprite_height // 2

def move_up():
    new_y = player.ycor() + 20
    if new_y < half_height - margin_y:
        player.sety(new_y)
    window.update()

def move_down():
    new_y = player.ycor() - 20
    if new_y > -half_height + margin_y:
        player.sety(new_y)
    window.update()

def move_left():
    new_x = player.xcor() - 20
    if new_x > -half_width + margin_x:
        player.setx(new_x)
    window.update()

def move_right():
    new_x = player.xcor() + 20
    if new_x < half_width - margin_x:
        player.setx(new_x)
    window.update()

def close_window():
    screen.bye()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(close_window, "Escape")

turtle.mainloop()