from utils import *
import time
import turtle
import random

# varible set up
Steeze = 0
Money = 0
Durability = 100
busy = False
BoardName = "Starter Board"
multiplier = 1

BoardLevel = 1
SwagLevel = 1
shop_open = False
auto_repair = False

# shop pricing
economy_scale = 3
earn_ratio = 0.070
drain = 5

set_background("SkatePart")
window.tracer(0)

# trick sprites
s1 = create_sprite("IdleBoard", 10, 10)
jump = create_sprite("JumpBoard", 10, 10)
olie = create_sprite("OlieBoard", 10, 10)
kick = create_sprite("KickBoard", 10, 10)
flip = create_sprite("FlipBoard", 10, 10)
around = create_sprite("360Board", 10, 10)
popshuv = create_sprite("shuvitboard", 10, 10)

for t in [popshuv, jump, olie, kick, flip, around]:
    t.hideturtle()

# making the text
def make_text(x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    return t

def write_outline(t, text, x, y, align="center", size=18):
    t.clear()
    t.color("black")
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        t.goto(x + dx, y + dy)
        t.write(text, align=align, font=("Arial", size, "bold"))
    t.color("white")
    t.goto(x, y)
    t.write(text, align=align, font=("Arial", size, "bold"))

m_stats = make_text(0, 240)
m_board = make_text(0, 200)
m_dura = make_text(0, 170)
m_trick = make_text(0, -180)
m_hint = make_text(0, -260)
m_shop = make_text(-320, -60)

# ui
def update_ui(tname, reward):
    write_outline(m_stats, f"STEZE: {Steeze} | MONEY: ${Money}", 0, 240)
    write_outline(m_board, f"{BoardName} (Lv{BoardLevel}) | MULT x{multiplier}", 0, 200, size=16)
    write_outline(m_dura, f"DURABILITY: {Durability} |", 0, 170, size=14)

    if tname:
        write_outline(m_trick, f"{tname}! +${reward}", 0, -180)
    else:
        m_trick.clear()

    write_outline(m_hint, "SPACE = Trick | B = Repair | E = Shop", 0, -260, size=12)

# makes the shop
def draw_shop():
    board_cost = int(300 * BoardLevel * economy_scale)
    swag_cost = int((200 + (SwagLevel * 200)) * economy_scale)
    auto_text = "OWNED" if auto_repair else "$4000"

    text = (
        "SHOP\n\n"
        f"1 Board Lv{BoardLevel} ${board_cost}\n"
        f"2 Swag Lv{SwagLevel} ${swag_cost}\n\n"
        f"N Auto Repair {auto_text}\n"
        "B Repair $100\n\n"
        "E Exit"
    )

    write_outline(m_shop, text, -320, -60, "left", 12)

def toggle_shop():
    global shop_open
    shop_open = not shop_open
    if shop_open:
        draw_shop()
    else:
        m_shop.clear()
        update_ui("", 0)

# money makin
def my_control():
    global Steeze, Money, Durability, busy

    if busy or Durability <= 0 or shop_open:
        return

    busy = True
    Steeze += 20 + (BoardLevel * 2)
    Durability -= drain

    s1.hideturtle()

    if Steeze >= 14000:
        trick, name, base = flip, "Backflip", 500
    elif Steeze >= 9000:
        trick, name, base = kick, "Kickflip", 250
    elif Steeze >= 6000:
        trick, name, base = around, "360", 150
    elif Steeze >= 3000:
        trick, name, base = jump, "Big Jump", 100
    elif Steeze >= 1500:
        trick, name, base = olie, "Ollie", 75
    else:
        trick, name, base = popshuv, "Pop Shuvit", 50

    trick.showturtle()
    window.update()
    time.sleep(0.25)
    trick.hideturtle()

    reward = int(base * multiplier * economy_scale * earn_ratio)
    Money += reward

    s1.showturtle()
    update_ui(name, reward)

    time.sleep(0.2)
    busy = False

# upgrader
def buy_board():
    global Money, BoardLevel, BoardName, multiplier, drain, Durability
    cost = int(300 * BoardLevel * economy_scale)

    if Money >= cost:
        Money -= cost
        BoardLevel += 1
        BoardName = f"Board Lv{BoardLevel}"
        multiplier += 1
        drain -= 1
        if drain == 1:
            drain = 0.5
            if drain <= 0:
                drain = 0

        Durability = 100
    update_ui("", 0)

def buy_swag():
    global Money, SwagLevel, multiplier
    cost = int((200 + (SwagLevel * 200)) * economy_scale)

    if Money >= cost:
        Money -= cost
        SwagLevel += 1
        multiplier += 1
    update_ui("", 0)

def repair_board():
    global Money, Durability

    if Money >= 100:
        Money -= 100
        Durability = 100

    update_ui("", 0)

    if shop_open:
        draw_shop()

# def get_skater():
#     global Money, NumSkaters, passincome
#     cost = int((500 + (NumSkaters * 500)) * economy_scale)

#     if Money >= cost:
#         Money -= cost
#         NumSkaters += 1

#         # YOUR SCALING (unchanged)
#         passincome = int((11.5 + NumSkaters ** 4) * 4)

#     update_ui("", 0)

def mech_repair():
    global Money, auto_repair
    if auto_repair:
        return
    if Money >= 4000:
        Money -= 4000
        auto_repair = True
    update_ui("", 0)

# Shop stuff
def shop_buy_1():
    if shop_open:
        buy_board(); draw_shop()
def shop_buy_2():
    if shop_open:
        buy_swag(); draw_shop()
def shop_buy_4():
    if shop_open:
        mech_repair(); draw_shop()

# contoling
window.onkeypress(my_control, "space")
window.onkeypress(repair_board, "b")
window.onkeypress(toggle_shop, "e")
window.onkeypress(shop_buy_1, "1")
window.onkeypress(shop_buy_2, "2")
window.onkeypress(shop_buy_4, "n")

window.listen()

# Looping stuff

update_ui("", 0)

while True:
    # Auto repair
    if auto_repair and Durability <= 5:
        repair_board()

    window.update()
    time.sleep(0.01)