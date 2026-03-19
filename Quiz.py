frog_points =  0
monkey_points = 0
dog_points = 0
print (" this a quiz to see if your a frog a monkey or dog")
input ("")
answer1 = input ("What type of season do you like A fall B winter C Summer D Spring")
if answer1 == ("A") or ("a"):
    monkey_points += 2
    dog_points += 1
if answer1 == ("B") or ("b"):
    frog_points += 1 
    monkey_points -= 1
if answer1 == ("C") or ("c"):
    dog_points += 2
if answer1 == ("D") or ("d"):
    monkey_points += 1
answer2 = input ("What type of biome do you like A Forest B swamp C Grassy field D rainforest")
if answer2 == ("A") or ("a"):
    monkey_points += 2
    dog_points += 1
if answer2 == ("B") or ("b"):
    frog_points += 2 
    monkey_points -= 1
if answer2 == ("C") or ("c"):
    dog_points += 2
if answer2 == ("D") or ("d"):
    monkey_points += 1
answer3 = input ("What type of food do you like A Bananas B Cooked Insects C Cooked Meat D Coconuts")
if answer3 == ("A") or ("a"):
    monkey_points += 2
    dog_points += 1
if answer3 == ("B") or ("b"):
    frog_points += 2 
    monkey_points -= 1
if answer3 == ("C") or ("c"):
    dog_points += 2
if answer3 == ("D") or ("d"):
    monkey_points += 1
if answer3 == ("C") and answer2 == ("C"):
    dog_points += 4
answer4 = input ("What type of activtys do you like A Talking to others B Exploring C Running around D Climbing trees")
if answer4 == ("A") or ("a"):
    monkey_points += 2
    dog_points += 1
if answer4 == ("B") or ("b"):
    frog_points += 2 
    monkey_points -= 1
if answer4 == ("C") or ("c"):
    dog_points += 2
if answer4 == ("D") or ("d"):
    monkey_points += 1
answer5 = input ("What type of places do you like A Social Place B Your home C Gyms D Rock Climbing gyms")
if answer3 == ("A") or ("a"):
    monkey_points += 2
    dog_points += 1
if answer3 == ("B") or ("b"):
    frog_points += 2 
    monkey_points -= 1
if answer3 == ("C") or ("c"):
    dog_points += 2
if answer3 == ("D") or ("d"):
    monkey_points += 1
if monkey_points > dog_points and monkey_points > frog_points:
    print ("your most matching with a Monkey!")
if dog_points > monkey_points and dog_points > frog_points:
    print ("you match most with a dog!")
if frog_points > dog_points and frog_points > monkey_points:
    print (" you match with frogs the most!")





