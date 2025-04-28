# Joshua Hamaker        04/03/2025
# Unit tests for guess.py

import pytest
from guess import generateNum, checkGuess, getGuess, playGame


def test_generateNum():
    assert 1 <= generateNum() <= 100


def test_checkGuess():
    assert checkGuess(50, 25) == "Too Low"
    assert checkGuess(50, 75) == "Too High"
    assert checkGuess(50, 50) == "Correct"


def test_getGuess_Correct(monkeypatch):
    monkeypatch.setattr("bullitins.input", lambda _: "42")
    assert getGuess() == 42