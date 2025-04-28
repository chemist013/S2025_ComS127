# Joshua Hamaker        04/23/25
# Lab 12 - Rock Paper Scissors

import random


def main() -> None:
    while True:
        print("How many games would you like to play? (enter an odd number)")
        numGames = input()
        try:
            numGames = int(numGames)
        except:
            print("Please enter an odd number")
            continue
        if numGames % 2 == 1:
            break
        else:
            print(f"{numGames} is not an odd number")
    winner = gameLoop(numGames)
    print(winner)
    


def generateComputerMove() -> str:
    moves = ["r", "p", "s"]
    return moves[random.randint(0, 2)]


def determineWinner(itemOne: str, itemTwo: str) -> int:
    choices = itemOne, itemTwo
    if choices[0] == choices[1]:
        return -1
    elif choices == ("r", "p") or choices == ("p", "s") or choices == ("s", "r"):
        return 1
    else:
        return 0


def playRound(playerInput) -> int:
    comInput = generateComputerMove()
    return determineWinner(playerInput, comInput)


def gameLoop(rounds: int) -> str:
    score = [0, 0]
    while True:
        print(f"Score: Human {score[0]}, CPU {score[1]}")
        while True:
            print("Pick [r]ock, [p]aper, or [s]cissors")
            playerChoice = input()
            if playerChoice in ["r", "p", "s"]:
                break
            else:
                print("Not a valid choice, please try again")
        winner = playRound(playerChoice)
        match winner:
            case 0:
                print("Human player won the round!")
                score[0] += 1
            case 1:
                print("Computer player won the round!")
                score[1] += 1
            case -1:
                print("The round was a tie!")
        if score[0] >= rounds // 2 + 1:
            return "Human player wins!"
        elif score[1] >= rounds // 2 + 1:
            return "Computer player wins!"


if __name__ == '__main__':
    main()