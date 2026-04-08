
from utils import *
set_background("moon")

s1 = create_sprite("Bart", 50, 100)

message1 = create_sprite("alien",-200,200)
message1.color("White")
message1.write("El Barto",font = ("New Times Roman", 40, "normal"))
message1.hideturtle()



window.update()
turtle.exitonclick()