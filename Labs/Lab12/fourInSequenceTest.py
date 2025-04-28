# Joshua Hamaker        04/11/2025
# Lab 12 - Unit Tests for fourInSequence

import fourInSequence

# DEBUGGING/ TESTING
# "." "X" "O"
# player 1 = X, 2 = O
testBoard =[[".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."]]

def test_checkForNextMoveWin():
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "X", "X", "X"]]
    assert fourInSequence.checkForNextMoveWin(testBoard, 1) == 3
    assert fourInSequence.checkForNextMoveWin(testBoard, 2) == -1
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "O", "O", "O"]]
    assert fourInSequence.checkForNextMoveWin(testBoard, 1) == -1
    assert fourInSequence.checkForNextMoveWin(testBoard, 2) == 3
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."]]
    assert fourInSequence.checkForNextMoveWin(testBoard, 1) == -1
    assert fourInSequence.checkForNextMoveWin(testBoard, 2) == -1


def test_checkAdjacent():
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "O"],
                [".", ".", ".", "X", "O", ".", "O"],
                [".", ".", "X", "X", "O", "X", "O"],
                [".", "X", "O", "O", "O", "X", "X"]]
    assert fourInSequence.checkAdjacent(testBoard, 1) in [0, 1, 2, 3, 4, 5]
    assert fourInSequence.checkAdjacent(testBoard, 2) in [3, 4, 5, 6]


def test_checkDraw():
    testBoard =[["X", "O", "X", "O", "X", "O", "X"],
                ["X", "O", "X", "O", "X", "O", "X"],
                ["O", "X", "O", "X", "O", "X", "O"],
                ["O", "X", "O", "X", "O", "X", "O"],
                ["X", "O", "X", "O", "X", "O", "X"],
                ["X", "O", "X", "O", "X", "O", "X"]]
    assert fourInSequence.checkDraw(testBoard) == True
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "O"],
                [".", ".", ".", "X", "O", ".", "O"],
                [".", ".", "X", "X", "O", "X", "O"],
                [".", "X", "O", "O", "O", "X", "X"]]
    assert fourInSequence.checkDraw(testBoard) == False


def test_checkWinner():
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "X", ".", "O"],
                [".", ".", ".", "X", "O", ".", "O"],
                [".", ".", "X", "X", "O", "X", "O"],
                [".", "X", "O", "O", "O", "X", "X"]]
    assert fourInSequence.checkWinner(testBoard, 1) == True
    assert fourInSequence.checkWinner(testBoard, 2) == False
    testBoard =[[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "O"],
                [".", ".", ".", "X", "O", "O", "O"],
                [".", ".", "X", "X", "O", "X", "O"],
                [".", "X", "O", "O", "O", "X", "X"]]
    assert fourInSequence.checkWinner(testBoard, 1) == False
    assert fourInSequence.checkWinner(testBoard, 2) == True
