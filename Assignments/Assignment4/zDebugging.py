import fourInSequence
import sys

def main() -> None:
    # DEBUGGING/ TESTING
    # "." "X" "O"
    # player 1 = X, 2 = O
    testBoard =[[".", ".", ".", ".", ".", ".", "."], # 0
                [".", ".", ".", ".", ".", ".", "."], # 1
                [".", ".", ".", ".", ".", ".", "."], # 2
                [".", ".", ".", ".", ".", ".", "."], # 3
                [".", ".", ".", "X", ".", ".", "."], # 4
                [".", ".", ".", "X", ".", ".", "."]] # 5
                # 0    1    2    3    4    5    6
    
    print(fourInSequence.checkAdjacent(testBoard, 1))
    sys.exit()

if __name__ == "__main__":
    main()