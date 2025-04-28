# Joshua Hamaker        03/01/2025
# Assignment 03 - NimGrab

# This is a game where players take sticks while trying to force their opponent to take the last stick
# The user can either play another human or a CPU

import random

def main() -> None:
    """ if __name__ == "main" """
    print("Welcome to NIMGRAB!")
    print("The classic game of risk & reward")
    print("Recreated w/ a CLI by Joshua Hamaker")
    print("for ComS 1270-2")
    print("")
    while True:
        scene = mainMenu()
        match scene:
            case "r":
                rules()
            case "c":
                gameLoopOnePlayer()
            case "h":
                gameLoopTwoPlayers()
            case "q":
                break


def mainMenu() -> str:
    """ The user interface for starting the game, viewing the rules or quitting the program """
    print("Would you like to [p]lay, see the [r]ules or [q]uit?")
    while True:
        choice: str = input()
        if choice == "p":
            print("Would you like to play against a [c]PU or another [h]uman?")
            while True:
                gameType: str = input()
                if gameType == "c" or gameType == "h":
                    print("")
                    return gameType
                else:
                    print("Please enter a valid option")
        elif choice == "r" or choice == "q":
            print("")
            return choice
        else:
            print("Please enter a valid option")


def rules() -> None:
    """ Prints the rules of NIMGRAB """
    print("The goal of NIMGRAB is to force your opponent to take the last stick.")
    print("There are initially 25 sticks and, on their turn, each player takes 1-3 of them.")
    print("This repeats until one player takes the last stick, who then loses.")
    print("")


def gameLoopOnePlayer() -> None:
    """ Organizes & controls the gameplay for one player mode (human vs CPU) """
    winner: bool = False
    numSticks: int = 25
    currentTurn: int = 1
    while not winner:
        if currentTurn != 0:
            updateCLI(numSticks)
        numSticks = takePlayerInput(currentTurn, numSticks)
        winner = checkWinner(numSticks)
        currentTurn = 1 if currentTurn == 0 else 0
    if currentTurn == 0:
        print("Player 1 took the last stick & lost")
    else: # currentTurn == 1
        print("The CPU took the last stick & lost")


def gameLoopTwoPlayers() -> None:
    """ Organizes & controls the gameplay for two player mode (human vs human) """
    winner: bool = False
    numSticks: int = 25
    currentTurn: int = 1
    while not winner:
        updateCLI(numSticks)
        numSticks = takePlayerInput(currentTurn, numSticks)
        winner = checkWinner(numSticks)
        currentTurn = 1 if currentTurn == 2 else 2
    if currentTurn == 2:
        print("Player 1 took the last stick & lost")
    else: # currentTurn == 1
        print("Player 2 took the last stick & lost")
    print("")


def updateCLI(s: int) -> None:
    """ Updates the terminal with a lexical and visual representation of the remaining sticks """
    print(f"Sticks remaining: {s}")
    print("| "*s)


def takePlayerInput(p: int, n: int) -> int:
    """ Handles prompting the user for input and validating said input """
    if p != 0:
        sticksTaken: int = 0
        print(f"How many sticks does player {p} take [1-3]?")
        valid: bool = False
        while not valid:
            sticksTaken = int(input())
            match n:
                case 2:
                    if sticksTaken == 1 or sticksTaken == 2:
                        valid = True
                    else:
                        print("Please enter a valid option")
                case 1:
                    if sticksTaken == 1:
                        valid = True
                    else:
                        print("Please enter a valid option")
                case _:
                    if sticksTaken == 3 or sticksTaken == 2 or sticksTaken == 1:
                        valid = True
                    else:
                        print("Please enter a valid option")
    else: # p == 0
        match n:
            case 3:
                sticksTaken = random.randint(1,2)
            case 2:
                sticksTaken = 1
            case _:
                sticksTaken = random.randint(1,3)
        print(f"The CPU took {sticksTaken} sticks")
    print("")
    return n - sticksTaken

def checkWinner(n: int) -> bool:
    """ Checks if a player or CPU has won the game """
    if n <= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()