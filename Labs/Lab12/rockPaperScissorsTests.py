# Joshua Hamaker       04/23/2025
# Lab 12 - Unit tests for 'rockPaperScissors.py'

import rockPaperScissors


def test_generateComputerMove():
    moves = ["r", "p", "s"]
    assert rockPaperScissors.generateComputerMove() in moves


def test_determineWinner():
    assert rockPaperScissors.determineWinner("r", "p") == 1
    assert rockPaperScissors.determineWinner("p", "r") == 0
    assert rockPaperScissors.determineWinner("p", "s") == 1
    assert rockPaperScissors.determineWinner("s", "p") == 0
    assert rockPaperScissors.determineWinner("s", "r") == 1
    assert rockPaperScissors.determineWinner("r", "s") == 0
    assert rockPaperScissors.determineWinner("r", "r") == -1
    assert rockPaperScissors.determineWinner("p", "p") == -1
    assert rockPaperScissors.determineWinner("s", "s") == -1