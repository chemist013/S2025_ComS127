# Joshua Hamaker        04/26/2025
# Assignment 6 - Candy Realm


import random
import sys


class Player:
    def __init__(self, isHuman: bool) -> None:
        self.isHuman = isHuman
        self.pos = 0


def main() -> None:
    print("Welcome to Candy Realm!")
    print("      Created by:      ")
    print("     Joshua Hamaker    ")
    print("      for ComS 127     ")
    print()
    menu()
    while True:
        print("How many human players are there (1-4):")
        numHumans = input()
        try:
            numHumans = int(numHumans)
            assert 1 <= numHumans <= 4
        except:
            print("Invalid input; Please enter a number 1-4")
            continue
        break
    print()
    board, deck, players = initVars(numHumans)
    turn = 0
    while True:
        currentPlayer = players[turn]
        if currentPlayer.isHuman: displayBoard(board, players)
        card = pickCard(deck, turn, currentPlayer.isHuman)
        movePlayer(board, card, currentPlayer)
        if currentPlayer.pos == len(board) - 1:
            displayBoard(board, players)
            break
        turn += 1
        if turn > 3: turn = 0
    print(f"Player {turn + 1} is the winner!")

def menu() -> None:
    while True:
        print("Would you like to [p]lay, read the [r]ules, or [q]uit?")
        choice = input()
        match choice:
            case "p":
                return
            case "r":
                rules()
            case "q":
                print()
                print("Thank you so much for playing my game")
                sys.exit()
            case _:
                print("Invalid input")


def rules() -> None:
    print("In Candy Realm, the goal is to reach the end of the board as quickly as possible")
    print("On your turn, you will be given two cards, and you (or a computer) will pick one")
    print("Your piece will then move to the next space that matches the color of the card you picked")
    print("(The last space on the board counts as any color)")
    print()


def initVars(humans: int) -> tuple[list[str], list[str], dict[int, Player]]:
    board = ["START"]
    for _ in range(6):
        board.append("R")
        board.append("O")
        board.append("Y")
        board.append("G")
        board.append("B")
        board.append("P")
    board.append("END")

    deck = []
    for _ in range(12):
        deck.append("R")
        deck.append("O")
        deck.append("Y")
        deck.append("G")
        deck.append("B")
        deck.append("P")
    for _ in range(7):
        random.shuffle(deck)
    
    players = {}
    for i in range(humans):
        players[i] = Player(True)
    for i in range(humans, 4):
        players[i] = Player(False)
    
    return board, deck, players


def displayBoard(board: list[str], players: dict[int, Player]) -> None:
    for i in players.keys():
        if players[i].pos == 0: print(f"  {i + 1}")
        else: print("      " + "   "*(players[i].pos - 1) + f" {i + 1}")

    for c in board:
        print(f"{c}  ", end="")
    print("\n")


def pickCard(deck: list[str], playerNum: int, playerType: bool) -> str:
    cardOne = deck.pop()
    cardTwo = deck.pop()
    if playerType: # if player is human
        print(f"\t1: {cardOne}\t2: {cardTwo}")
        print(f"Player {playerNum + 1}, pick a card (1, 2)")
        while True:
            choice = input()
            try:
                choice = int(choice)
                assert choice == 1 or choice == 2
            except:
                print("Please enter either 1 or 2")
                continue
            break
    else:
        choice = random.randint(1, 2)
    if choice == 1: return cardOne
    else: return cardTwo


def movePlayer(board: list[str], card: str, player: Player) -> None:
    try:
        moveTarget = board.index(card, player.pos + 1)
    except ValueError:
        player.pos = len(board) - 1
        return
    player.pos = moveTarget
        

if __name__ == '__main__':
    main()