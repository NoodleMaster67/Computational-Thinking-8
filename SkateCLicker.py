from utils import *
import time
import turtle

# ---------------- CORE ----------------
Steeze = 0
Money = 0
Durability = 100
busy = False

BoardLevel = 1
SwagLevel = 0
BoardName = "Starter Board"
multiplier = 1
earn_ratio = 0.1
unlocked_tricks = set()

last_trick_time = 0
TRICK_COOLDOWN = 0.8

# ---------------- SETUP ----------------
set_background("SkatePart")
window.tracer(0)

s1 = create_sprite("IdleBoard", 10, 10)

jump = create_sprite("JumpBoard", 10, 10)
olie = create_sprite("OlieBoard", 10, 10)
kick = create_sprite("KickBoard", 10, 10)
flip = create_sprite("FlipBoard", 10, 10)
around = create_sprite("360Board", 10, 10)

for t in [jump, olie, kick, flip, around]:
    t.hideturtle()

# ---------------- GAME ----------------
def do_trick():
    global Steeze, Money, Durability, combo, last_trick_time

    if time.time() - last_trick_time < TRICK_COOLDOWN:
        return

    last_trick_time = time.time()

    if Durability <= 0:
        update_ui("Board broken", 0)
        return

    Steeze += int((20 + BoardLevel * 2) * multiplier)

    s1.hideturtle()

    if Steeze >= 8000:
        trick, name, base = flip, "Backflip", 1000
    elif Steeze >= 5000:
        trick, name, base = kick, "Kickflip", 500
    elif Steeze >= 3000:
        trick, name, base = around, "360", 300
    elif Steeze >= 1500:
        trick, name, base = jump, "Jump", 150
    else:
        trick, name, base = olie, "Ollie", 50

    trick.showturtle()
    window.update()
    time.sleep(0.15)
    trick.hideturtle()

    Money += reward

    draw_text(m_trick, f"{name} +{reward}", 0, -220)
    draw_text(m_stats, f"Steeze {Steeze} Money {Money} Combo {combo}", 0, 260)

# ---------------- SHOP ----------------
def buy_board():
    global Money, BoardLevel, multiplier, Durability

    cost = 300 * BoardLevel

    if Money >= cost:
        Money -= cost
        BoardLevel += 1
        multiplier += 1
        Durability = 100

def buy_swag():
    global Money, SwagLevel, multiplier

    cost = 200 + SwagLevel * 200

    if Money >= cost:
        Money -= cost
        SwagLevel += 1
        multiplier += 1

def repair():
    global Money, Durability

    if Money >= 100:
        Money -= 100
        Durability = 100

# ---------------- INPUT (SAFE VERSION) ----------------
def press_space():
    global holding_space
    holding_space = True
#     reset_bar()

# def release_space():
#     global holding_space
#     holding_space = False
#     do_trick()

window.onkeypress(do_trick, "space")
window.onkeypress(buy_board, "1")
window.onkeypress(buy_swag, "2")
window.onkeypress(repair, "b")

window.listen()

# reset_bar()
# draw_bar()

# ---------------- LOOP ----------------
while True:
    time.sleep(0.01)
    # update_bar()
    window.update()