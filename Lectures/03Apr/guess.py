# Joshua Hamaker        04/03/2025
# Random number guessing game

import random

def main() -> None:
    secretNumber = generateNum()
    attempts = playGame(secretNumber)
    print(f"You guessed the number in {attempts} attempts!")


def generateNum() -> int:
    sNum = random.randint(1,100)
    return sNum


def checkGuess(sNum: int, guess: int) -> str:
    if guess < sNum:
        return "Too Low!"
    elif guess > sNum:
        return "Too High!"
    else:
        return "Correct!"


def getGuess() -> int:
    print("Enter your guess:")
    while True:
        i = input()
        try:
            i = int(i)
        except ValueError:
            print("Please input an intiger")
            continue
        if i >= 1 and i <= 100:
            return i
        print("Please enter a number between 1 and 100")


def playGame(sNum: int) -> int:
    pass


if __name__ == '__main__':
    main() 