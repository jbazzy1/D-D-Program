# D&D Game for Integration Project                                      COP1500
# By __Jacob-Bazzy__
# Character Creation

import random

fourSidedDie = random.randint(1, 4)
eightSidedDie = random.randint(1, 8)
twelveSidedDie = random.randint(1, 12)

optionsForFleeing = ('Flee', 'flee')
optionsForAttacking = ('Attack', 'attack')
optionsForBargaining = ('Bargain', 'bargain')


def save():
    saveFile = open("D&D Save File", 'w')
    saveFile.write("NAME: " + characterName)
    saveFile.write("\nCLASS: " + characterClass)
    saveFile.write("\nHP: " + str(hitPoints))
    saveFile.write("\nSTR: " + str(strStat))
    saveFile.write("\nDEX: " + str(dexStat))
    saveFile.write("\nCHAR: " + str(charStat))
    saveFile.write("\nCONST: " + str(constStat))
    saveFile.write("\nINT: " + str(intStat))
    saveFile.write("\nWIS: " + str(wiseStat))
    saveFile.close()
    print("\nGame saved!")


def combat():
    monsterHP = 10
    while monsterHP > 0:
        if combatInput in optionsForFleeing:
            totalEightOutcome = eightSidedDie + dexStat
            if totalEightOutcome >= 6:
                print("You roll an eight sided die for", eightSidedDie)
                print("You flee like a coward.")
                monsterHP = 0
            else:
                currentHP = hitPoints - 2
                print("You roll an eight sided die for", eightSidedDie)
                print("You trip and fall!", int(currentHP), "HP remaining.")
                monsterHP = 0
        elif combatInput in optionsForAttacking:
            totalTwelveOutcome = twelveSidedDie + strStat
            if totalTwelveOutcome >= monsterHP:
                print("You roll a twelve sided die for", twelveSidedDie)
                print(
                    "Critical hit! You slay the monster with ease, "
                    "taking it down in one hit.")
                monsterHP = 0
            else:
                monsterHP -= totalTwelveOutcome
                print("You hit the monster for", totalTwelveOutcome,
                      ". It has",
                      monsterHP, "remaining.")
                monsterHP = 0
        else:
            print("You attempt bargaining for your life.")
            bargainForLife = fourSidedDie + charStat
            if bargainForLife >= 10:
                print("The monster laughs at your attempt to speak to them "
                      "and lets you by.")
                monsterHP = 0
            else:
                currentHP = hitPoints - bargainForLife
                print("Confused, the monster picks you up and tosses you off "
                      "a cliff.")
                print("You have", currentHP, "HP remaining.")
                monsterHP = 0


# Added sep and end to meet requirements.
print("Welcome to D&D", "!", sep="", end=" ")
input("To begin creating your character, press enter.\n")
while True:
    characterName = input("Choose your HERO's name: \n")
    characterClass = input("\nSelect your CLASS: "
                           "\nWARRIOR, ROGUE, MAGE, ARCHER\n")

    if characterClass == "Archer" or characterClass == "archer" or \
            characterClass == "ARCHER":
        print("\nGreetings,", characterName + "! "
                                              "You have chosen to be an",
              characterClass + "!")  # Fixes grammar issue (not "a archer")
    else:
        print("\nGreetings,", characterName + "! You have chosen to be a",
              characterClass)

    print("\nYou have 35 points to allocate to six different attributes: "
          "\nSTRENGTH, DEXTERITY, CHARISMA, CONSTITUTION, INTELLIGENCE, and "
          "WISDOM.\n")

    totalStatPoints = int(
        35)  # Total number of stat points that will eventually reach 0
    while True:
        strStat = int(float(input(
            "Enter a number between 3 and 10 for STRENGTH: ")))
        if 3 <= strStat <= 10:
            # Takes totalStatPoints variable and subtracts by number input
            # by the user; continues pattern for rest of stats
            statPointsRemaining1 = totalStatPoints - strStat
            print("\nYou have", statPointsRemaining1, "points remaining.\n")
            break
        else:
            print("Try again")

    while True:
        dexStat = int(float(input(
            "Enter a number between 3 and 10 for DEXTERITY: ")))
        if 3 <= dexStat <= 10:
            statPointsRemaining2 = statPointsRemaining1 - dexStat
            print("\nYou have", statPointsRemaining2, "points remaining.\n")
            break
        else:
            print("Try again")

    while True:
        charStat = int(float(input(
            "Enter a number between 3 and 10 for CHARISMA: ")))
        if 3 <= charStat <= 10:
            statPointsRemaining3 = statPointsRemaining2 - charStat
            print("\nYou have", statPointsRemaining3, "points remaining.\n")
            break
        else:
            print("Try again")

    while True:
        constStat = int(float(input(
            "Enter a number between 3 and 10 for CONSTITUTION: ")))
        if 3 <= constStat <= 10:
            statPointsRemaining4 = statPointsRemaining3 - constStat
            print("\nYou have", statPointsRemaining4, "points remaining.\n")
            break
        else:
            print("Try again")

    while True:
        intStat = int(float(input(
            "Enter a number between 3 and 10 for INTELLIGENCE: ")))
        if 3 <= intStat <= 10:
            statPointsRemaining5 = statPointsRemaining4 - intStat
            print("\nYou have", statPointsRemaining5, "points remaining.\n")
            break

        else:
            print("Try again")

    wiseStat = int(float(
        input("Enter a number between 3 and 10 for WISDOM: ")))  # WISDOM stat
    if 3 <= wiseStat <= 10:
        statPointsRemaining6 = statPointsRemaining5 - wiseStat

    if statPointsRemaining6 == 1:
        print("\nYou have", statPointsRemaining6,
              "point remaining.\n")  # Turns "1 points left" to "1 point left"
    else:
        print("\nYou have", statPointsRemaining6, "points remaining.\n")

    hitPoints = 10 + strStat

    if statPointsRemaining6 != 0:  # Stat Sheet
        print("Sorry! These stats cannot be used. Please try again.\n")
    else:
        print("\nStat Sheet:\n")
        print("NAME =", characterName)
        print("CLASS =", characterClass)
        # HP has a base number and changes based on input for strStat
        print("HP =", hitPoints)
        print("STR =", strStat)
        print("DEX =", dexStat)
        print("CHAR =", charStat)
        print("CONST =", constStat)
        print("INT =", intStat)
        print("WIS =", wiseStat)
        break

save()
print(
    "\nTo move forward with your adventure, you must answer these questions.")

exponentInput = int(input(
    "\nWhat is the output of 3**3?\n"))  # Required for Integration Project
exponentAnswer = 3 ** 3
if exponentInput == exponentAnswer:
    print("Great job!\n")
else:
    print("That is incorrect. The correct answer is 27.\n")

floorDivisionInput = int(input(
    "\nWhat is the output of 121//5?\n"))  # Required for Integration Project
floorDivisionAnswer = 121 // 5
if floorDivisionInput == floorDivisionAnswer:
    print("Great job!\n")
else:
    print("That is incorrect. The correct answer is 24.\n")

modulusInput = int(input(
    "\nWhat is the output of 128%9?\n"))  # Required for Integration Project
modulusAnswer = 128 % 9
if modulusInput == modulusAnswer:
    print("Great job!\n")
else:
    print("That is incorrect. The correct answer is 2.\n")

# Required for Integration Project
equationInput = int(input(
    "\nWhat is the output of 21/3+2*4-1?\n"))
equationAnswer = 21 / 3 + 2 * 4 - 1
if equationInput == equationAnswer:
    print("Great job!\n")
else:
    print("That is incorrect. The correct answer is 14.\n")

# Required for Integration Project
stringMultiplicationInput = input(
    "\nWanna see the word 'Goblin' printed 21 times? (Y/N)\n")
stringMultiplication = "Goblin" * 21
if stringMultiplicationInput == "Y" or stringMultiplicationInput == "y":
    print(stringMultiplication)
    print("\nThat's a lot of goblins!")
else:
    print("\nToo bad\n")
    print(stringMultiplication)

print("\nYou are just about ready to embark on your adventure!")

input("You encounter a terrible-looking ogre")

combatInput = input("What do you do? (Attack, Flee, Bargain)")

combat()
save()
print("Done!")
