import random

miles_traveled: int = 0
thirst = 0
horse_tiredness = 0
distance_m = -20
number_d = 3
sanctuary = random.randrange(1, 21)
monsters_traveled = miles_traveled - distance_m

print("Welcome to Temple Run.txt, you have stolen an ancient idol from a temple that is situated deep in the mountains."
      )
print("The monsters guarding the temple"
      " want their idol back and are chasing you down! "
      "Survive your archeological exploit and")
print("outrun the monsters on your trusty steed!")
done = False
while not done:
    print("")
    print("""A. Drink from your canteen. 
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.""")
    letter = input("Your Choice? ")
    if miles_traveled >= 200:
        print("You survived and escaped the monsters! To play the game again, press r.")
        done = True
    if thirst >= 6:
        print("You died from dehydration, press r to try again.")
        done = True
    if not done and thirst >= 4:
        print("You are thirsty.")
    if monsters_traveled <= 0:
        print("The monsters caught you, press r to try again.")
        done = True
    if horse_tiredness >= 8:
        print("Your horse died from exhaustion, you are unable to continue, press r to try again.")
        done = True
    if not done and distance_m <= 15:
        print("The monsters are getting close! I can almost hear them breathing.")
    if done:
        restart = input("Would you like to try again? ")
        if restart.lower() == "r":
            done = False
            miles_traveled: int = 0
            thirst = 0
            horse_tiredness = 0
            distance_m = -20
            number_d = 3
            monsters_traveled = distance_m - miles_traveled

    if letter.lower() == "a":
        if number_d >= 1:
            print("You drank one of your flasks of water.")
            number_d -= 1
            thirst -= 20
            print("You have", number_d, "drinks left")
            miles_traveled += random.randrange(3, 10)
            thirst += 1
            horse_tiredness += random.randrange(1, 3)
            distance_m += random.randrange(7, 14)
        else:
            print("You don't have water left.")
            miles_traveled += random.randrange(3, 10)
    elif letter.lower() == "b":
        print("Your speed is now 15 miles an hour.")
        miles_traveled += random.randrange(5, 13)
        thirst += 1
        horse_tiredness += random.randrange(1, 3)
        distance_m += random.randrange(7, 14)
        print("You have travelled", miles_traveled, "miles.")
        if not done and sanctuary == 1:
            print("You found an ancient sanctuary containing a well of potable fresh water!")
            horse_tiredness = 0
            thirst = 0
            number_d = 3
    elif letter.lower() == "c":
        print("You are travelling at 25 miles an hour.")
        miles_traveled += random.randrange(10, 21)
        thirst += 1
        horse_tiredness += random.randrange(1, 3)
        distance_m += random.randrange(7, 14)
        print("You have travelled", miles_traveled, "miles.")
        if not done and sanctuary == 1:
            print("You found an ancient sanctuary containing a well of potable fresh water!")
            horse_tiredness = 0
            thirst = 0
            number_d = 3

    elif letter.lower() == "d":
        print("You have stopped to rest.")
        horse_tiredness -= (10, 50)
        distance_m += random.randrange(7, 14)
        print("Your horse is happy!")
    elif letter.lower() == "e":
        print("""Here is a list of what you have, the number of miles that you have travelled, 
and your distance from the monsters.""")
        print("You have travelled", miles_traveled, "miles.")
        print("The monsters are", abs(monsters_traveled), "miles behind you.")
        print("You have", number_d, "drinks left.")
    if letter.lower() == "q":
        quit = input("Are you sure you want to quit? Y/N ")
        if quit.lower() == "y":
            done = True
            print("You have quit the game.")
        elif quit.lower() == "n":
            var = letter.lower() == "e"
