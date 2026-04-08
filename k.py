team_points = 0
money_points = 20
chem_points = 5
import sys
import random
full_names = {
    "Steph": "Stephen Curry",
    "Cade": "Cade Cunningham",
    "Darius": "Darius Garland",
    "Isaiah": "Isaiah Collier",
    "Bronny": "Bronny James",
    "Kobe": "Kobe Bryant",
    "Ray": "Ray Allen",
    "Jordan": "Jordan Poole",
    "Tracy": "Tracy McGrady",
    "Ben": "Ben Simmons",
    "Larry": "Larry Bird",
    "Kevin": "Kevin Durant",
    "Franz": "Franz Wagner",
    "Draymond": "Draymond Green",
    "Jeremy": "Jeremy Sochan",
    "Dirk": "Dirk Nowitzki",
    "Shawn": "Shawn Kemp",
    "Pascal": "Pascal Siakam",
    "Obi": "Obi Toppin",
    "Spud": "Spud Webb",
    "Shaq": "Shaquille O'Neal",
    "Victor": "Victor Wembanyama",
    "Jarret": "Jarrett Allen",
    "Myles": "Myles Turner",
    "Al": "Al Jefferson",
    "Phil": "Phil Jackson",
    "Doc": "Doc Rivers",
    "Kenny": "Kenny Atkinson",
    "Roy": "Roy Rubin",
    "Steve": "Steve Nash",
    "Ochai": "Ochai Ajbaji",
    "Roba": "Roba Gezahegn",
    "Jalen": "Jalen Duren",
    "2k": "2k My Player"

}
print("")
print("")
print("you have 20 dollars to create the best NBA team")
print("=== Press Enter to start ===")
input("")
print("---------------------------------------------------------------------------------------------")
print("First Choose a team Name")
print("If your good enough you will play against the 2017 playoff line up if you were in the Western conference")
team = input("Enter team name: ")
if team == ("Jayhawks"):
    money_points += 10000
print ("Choose a Difficulty | easy 25$| Normal 20$| Hard 15$|")
difficulty = input("==").strip().capitalize()
if difficulty == ("Easy"):
    money_points += 5
if difficulty == ("Hard"):
    money_points -= 5
print("---------------------------------------------------------------------")
print(f"Remeber you only have {money_points}$ to choose your starting five plus a coach")
print("Also be carful who you choose because some players have hidden chemistry debuffs")
Check = input("Type CD if you want to see the chemistry debuffs Or press enter to skip ")
if Check == ("CD"):
    print("--------------------------------------------------------------------------------")
    print("You'll start with five chemstry points if it goes below zero your team will suck")
    print("4 Chem points: -3 team points")
    print("3 Chem points: -2 team points")
    print("2 Chem points: -2 team points")
    print("1 Chem points: -3 team points")
    print("These debuffs do stack")
    Check2 = input("To learn more about what team points do type (TP) Or press enter to skip")
    if Check2 == ("TP") or Check2 == ("Tp") or Check2 == ("tp"):
        print("Team points is what helps dertermine what your record will be, and how you will perform in the playoffs")
        print("Press Enter to continue")
input("")
print("to choose type the players first name with no spaces after their name")
print ("Make sure that you spell their name correctly")
print("Press Enter to start draft")
input ("")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()
print("------------------------------------------------------------------------------------------------")
print(f"Money Left: {money_points}$")
print("Your point guard |5$ Steph Curry |4$ Cade Cunningham or Gary paton |3$ Darius Garland |2$ Isaiah Collier |1$ Bronny james |")
pg = input("== ").strip().capitalize()
full_pg = full_names.get(pg, pg)
if pg == ("Steph"):
    money_points -= 5
    team_points += 9
    if random.randint(1, 7) == 1:
        print ("Steph Had a meeting with Benjiman")
elif pg == ("Cade"):
    money_points -= 4
    team_points += 7
elif pg == ("Gary"):
    money_points -= 4
    team_points += 8
    chem_points -= 1
elif pg == ("Darius"):
    money_points -= 3
    team_points += 7
elif pg == ("Isaiah"):
    money_points -= 2
    team_points += 3
elif pg == ("Bronny"):
    money_points -= 1
    team_points += 1
elif pg == ("Ochai"):
    team_points += 100
    money_points -= 20
elif pg == ("Roba"):
    chem_points += 1000
    team_points += 100
else:
    print ("you spelt their name wrong")
    print ("so you received Darius garland!")
    pg == ("Darius")
    money_points -= 3
    team_points += 7
print("")
print("")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()
print("---------------------------------------------------------------------------------------------------------")
print(f"Money Left: {money_points}$")
print("choose shooting guard |5$ Kobe Bryant |4$ Ray allen |3$ Jordan poole |2$  Washed Tracy Mcgrady|1$ Ben simmons |---")
sg = input("==").strip().capitalize()
full_sg = full_names.get(sg, sg)
if sg == ("Kobe"):
    money_points -= 5
    team_points += 10
    chem_points -= 1
    if random.randint(1, 15) == 1:
        print("Kobe Had a bad trip in colorado and got suspended 1/15 chance")
        team_points -= 15
        chem_points -= 1
elif sg == ("Ray"):
    money_points -= 4
    team_points += 7
elif sg == ("Jordan"):
    money_points -= 3
    team_points += 5
elif sg == ("Tracy"):
    money_points -= 2
    team_points += 3
elif sg == ("Ben"):
    money_points -= 1
    team_points += 1
    chem_points += 2
elif sg == ("Kevin mcroller"):
    team_points += 100
    chem_points += 100
print("")
print("")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()
# Choose Small forward
print("---------------------------------------------------------------------------------------------------------")
print(f"Money Left: {money_points}$")
print(" Choose Small Forward |5$ Larry Bird |4$ Kevin Durant |3$ Franz Wagner |2$ Draymond green |1$ Jeremy Sochan |")
sf = input("==").strip().capitalize()
full_sf = full_names.get(sf, sf)
if sf == ("Larry"):
    money_points -= 5
    team_points += 10
    chem_points -= 1
elif sf == ("Kevin"):
    money_points -= 4
    team_points += 10
    if random.randint(1, 5) == 1:
        print("------------------------------------------------")
        print("KD's Burner got leaked -3 Chem points 1/5 chance")
        chem_points -= 3
elif sf == ("Franz"):
    money_points -= 3
    team_points += 6
elif sf == ("Draymond"):
    money_points -= 2
    team_points += 4
    if random.randint(1, 10) == 1:
        print("----------------------------------------------------")
        print(f"Draymond Punched {pg}! you lost two chemistry points!")
        chem_points -= 2
elif sf == ("Jeremy"):
    money_points -= 1
    team_points += 1
    chem_points -= 2
print("")
print("")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()
if sg == ("Jordan") and sf == ("Draymond"):
    chem_points -= 3
    print("Draymond Punched JP! Lose 3 Chemistry Points")
print("---------------------------------------------------------------------------------------------------------")
print(f"Money Left: {money_points}$")
print("Your Power Forward |5$ Dirk Nowitzki |4$ Shawn kemp |3$ Pascal Siakam |2$ Obi Toppin |1$ Spud web |")
pf = input("==").strip().capitalize()
full_pf = full_names.get(pf, pf)
if pf == ("Dirk"):
    money_points -= 5
    team_points += 9
elif pf == ("Shawn"):
    money_points -= 4
    team_points += 7
elif pf == ("Pascal"):
    money_points -= 3
    team_points += 5
elif pf == ("Obi"):
    money_points -= 2
    team_points += 3
elif pf == ("Spud"):
    money_points -= 1
    team_points += 1
    chem_points -= 2
print("")
print("")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()

print("----------------------------------------------------------------------------------------------")
print(f"Money Left: {money_points}$")
print("Your c |5$ Shaq O'neil |4$ Victor wembaya |3$ Jarret Allen or Jalen Duren |2$ Myles Turner |1$ Al Jefferson |")
c = input("==").strip().capitalize()
full_c = full_names.get(c, c)
if c == ("Shaq"):
    money_points -= 5
    team_points += 10
    chem_points -= 1
elif c == ("Victor"):
    money_points -= 4
    team_points += 7
elif c == ("Jarret"):
    money_points -= 3
    team_points += 5
elif c == ("Jalen"):
    money_points -= 3
    team_points += 6
elif c == ("Myles"):
    money_points -= 2
    team_points += 3
elif c == ("Al"):
    money_points -= 1
    team_points += 1
print("")
print("")
print("-------------------------------------------------------------------------------------------------")
if money_points <= 0:
    print("You ran out of Money!")
    sys.exit()
print(f"Money Left: {money_points}$")
print("Your coach |5$ Phil jackson |4$ Doc rivers |3$ Kenny Atkinson |2$ Roy Rubin |1$  Steve Nash |")
coach = input("==").strip().capitalize()
full_coach = full_names.get(coach, coach)
if coach == ("Phil"):
    money_points -= 5
    team_points += 20
elif coach == ("Doc"):
    money_points -= 4
    team_points += 7
elif coach == ("Kenny"):
    money_points -= 3
    team_points += 4
elif coach == ("Roy"):
    money_points -= 2
    team_points += 1
elif coach == ("Steve"):
    money_points -= 1
    team_points += 0
print("")
print("")
if money_points < 0:
    print("You ran out of Money!")
    sys.exit()
if chem_points <= 4:
    team_points -= 3
if chem_points <= 3:
    team_points -= 2
if chem_points <= 2:
    team_points -= 2
if chem_points <= 1:
    team_points -= 3
if chem_points <= 0:
    team_points -= 20
    print("L team Chem so team sucks")
if pg == ("Russell") and sf == ("Kevin"):
    team_points -= 5
    chem_points -= 2
    print("You put kd and russ together bad idea -2 Chem points and -5 team points")
if random.randint(1, 15) == 1:
    print (f"uh oh {c} got injured and will be doing half as good")
max_points = 40
games = 82
win_pct = team_points / max_points
wins = round(win_pct * games)
losses = games - wins
if wins > 82:
    wins -= wins
    wins += 82
    losses = 0
print("---------------------------------------------------------------------------------------------------------")
print(f"Team Points: {team_points}")
print(f"Your Season Record: {wins}-{losses}")
input("")
print ("press enter to continue")

if wins > 60:
    random.randint(1, 8)
    if random == 1 or random == 2:
        mvp = sg
        team_points += 3
    if random == 3 or random == 4:
        mvp = sg
    if random == 5:
        mvp = sf
    if random == 6:
        mvp = pf
    if random == 7 or random == 8:
        mvp = ("Lebron James")
if wins < 60
    mvp == ("Lebron")

def simulate_game(team_rating, opponent_rating):
    team_score = random.randint(90, 115)
    opponent_score = random.randint(90, 115)
    diff = team_rating - opponent_rating
    team_score += int(diff * random.uniform(0.3, 0.7))
    opponent_score += int(-diff * random.uniform(0.3, 0.7))
    if random.randint(1, 6) == 1:
        opponent_score += random.randint(5, 15)
    return max(team_score, 80), max(opponent_score, 80)
def play_series(team_name, opponent_name, team_rating, opponent_rating):
    team_wins = 0
    opponent_wins = 0
    game = 1
    print("===================================")
    print(team_name, "vs", opponent_name)
    while team_wins < 4 and opponent_wins < 4:
        input("Press Enter")
        t, o = simulate_game(team_rating, opponent_rating)
        print(team_name, t, "-", o, opponent_name)
        if t > o:
            team_wins += 1
        else:
            opponent_wins += 1
        print("Series:", team_wins, "-", opponent_wins)
        game += 1
    return team_wins > opponent_wins
print("-----------------------------------------------------------------------------------------------------")
print("YOU MADE THE WESTERN CONFERENCE PLAYOFFS")
print("== Current Lineup ==")
print(f"PRESENTING THE 2017 {team}!")
print(f"PG: {full_pg}")
print(f"SG: {full_sg}")
print(f"SF: {full_sf}")
print(f"PF: {full_pf}")
print(f"C: {full_c}")
print(f"Coach: {full_coach}")
print("Press Enter to continue")
input("")
print("First Round")
input("")
if not play_series(team, "Trail Blazers", int(wins*0.95), 45):
    print("Lost Round 1")
    sys.exit()
print("---------------------------------------------------------------------------------------------------------")
print("2nd Round")
input("")
if not play_series(team, "Jazz", int(wins*0.9), 52):
    print("Lost in the Conference Semifinals")
    sys.exit()
print("---------------------------------------------------------------------------------------------------------")
print("3rd Round")
input("")
if not play_series(team, "Spurs", int(wins*0.85), 60):
    print("Lost in the Conference Finals")
    sys.exit()
print("---------------------------------------------------------------------------------------------------------")
print("You made it to the finals! you'll be playing prime lebron good luck!")
input("")
if play_series(team, "Cleveland Cavaliers", int(wins*0.8), 62):
    print("You won the NBA Finals!")
    champion = True
else:
    print("Lost in the NBA Finals")
    champion = False
print("SEASON SUMMARY")
print(f"Record: {wins}-{losses}")
print(f"MVP: {mvp}")
print(f"PG: {full_pg}")
print(f"SG: {full_sg}")
print(f"SF: {full_sf}")
print(f"PF: {full_pf}")
print(f"C: {full_c}")
print(f"Coach: {full_coach}")
print (f"Difficulty: {difficulty}")
print (f"With {money_points}$ Left to spare")
if champion:
    print(" 2017 NBA WORLD CHAMPIONS! ")
else:
    print("Better luck next season")
