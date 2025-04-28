# Joshua Hamaker        02/21/2024
# Lab05 - Adventure Story

# 
# 

import random

def main() -> None:
    hasKnife = False
    hasMusicBox = False
    print("Welcome to Adventure Story!")
    print("A poorly titled CLI game by Joshua Hamaker")
    print("for ComS 1270-2")
    print("")
    print("")
    print("You hastily enter a shack and quickly lock the door behind you.")
    print("You hear the sound of a large monster approaching.")
    print("You see a hallway with a door at the end to your [l]eft and to your [r]ight.")
    print("Or you can go [b]ack and leave the shack now, but the monster will surely catch you.")
    print("Which way do you choose?")
    isValid: bool = False
    while not isValid:
        choiceInitial = input("")
        if choiceInitial == "l" or choiceInitial == "r" or choiceInitial == "b":
            isValid = True
        else:
            print("Please enter a valid choice.")
    match choiceInitial:
        case "l":
            print("You run down the hallway and reach the door at the end.")
            print("You attempt to open the door but it appears to be locked.")
            print("Do you attempt to [p]ick the lock or go [b]ack the way you came?")
            isValid= False
            while not isValid:
                choiceLeft = input("")
                if choiceLeft == "p" or choiceLeft == "b":
                    isValid = True
                else:
                    print("Please enter a valid choice.")
            match choiceLeft:
                case "p":
                    if random.randint(0, 1) == 1:
                        print("You successfully pick the lock and open the door.")
                        print("You find yourself in a kitchen.")
                        print("You see a knife on the counter.")
                        print("Do you [t]ake the knife or [l]eave it?")
                        isValid = False
                        while not isValid:
                            choiceKnife = input("")
                            if choiceKnife == "t" or choiceKnife == "l":
                                isValid = True
                            else:
                                print("Please enter a valid choice.")
                        match choiceKnife:
                            case "t":
                                hasKnife = True
                                print("You got a knife!")
                                print("It glimmers in the moonlight from the kitchen window.")
                                print("You run back the way you came.")
                            case "l":
                                print("You leave the knife on the counter.")
                                print("You run back the way you came.")
                    else:
                        print("You fail to pick the lock.")
                        print("You run back the way you came.")
                case "b":
                    print("You run back the way you came.")
        case "r":
            print("You run down the hallway and reach the door at the end.")
            print("You open the door and find yourself in a bedroom.")
            print("You see a bed and a dresser.")
            print("On the dresser you see a music box.")
            print("Do you [t]ake the music box or [l]eave it?")
            isValid = False
            while not isValid:
                choiceMusicBox = input("")
                if choiceMusicBox == "t" or choiceMusicBox == "l":
                    isValid = True
                else:
                    print("Please enter a valid choice.")
            match choiceMusicBox:
                case "t":
                    hasMusicBox = True
                    print("You got a music box!.")
                    print("It plays a haunting melody.")
                    print("You run back the way you came.")
                case "l":
                    print("You leave the music box on the dresser.")
                    print("You run back the way you came.")
            print("You run back the way you came.")
        case "b":
            print("As you turn around to unlock the door, the monster breaks through.")
    print("The monster stands in front of a broken door.")
    print("You have no choice but to face it.")
    if hasKnife:
        print("You can [f]ight the monster with your knife.")
    if hasMusicBox:
        print("You can [p]lay the music box to distract the monster.")
    if hasMusicBox or hasKnife:
        print("Or you can [r]un away.")
    else:
        print("All you can do is [r]un away.")
    print("What do you do?")
    isValid = False
    while not isValid:
        choiceMonster = input("")
        if choiceMonster == "r" or (choiceMonster == "f" and hasKnife == True) or (choiceMonster == "p" and hasMusicBox == True):
            isValid = True
        else:
            print("Please enter a valid choice.")
    match choiceMonster:
        case "f":
            print("You fight the monster with your knife.")
            print("You manage to kill the monster.")
            print("You run past it and out the door to safety.")
            print("YOU WIN!")
            print("(Bad ending)")
        case "p":
            print("You pull out the music box and play it.")
            if random.randint(0, 1) == 1:
                print("The monster is distracted by the music box.")
                print("You run past it and out the door to safety.")
                print("YOU WIN!")
                print("(Good ending)")
            else:
                print("The monster is not distracted by the music box.")
                print("It lunges at you and you are eaten.")
                print("GAME OVER")
        case "r":
            print("You attempt to run past the monster but it is no use.")
            print("It catches you and eats you.")
            print("GAME OVER")

if __name__ == "__main__":
    main()