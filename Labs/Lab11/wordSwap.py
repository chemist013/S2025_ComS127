# Joshua Hamaker        04/04/2025
# Lab 11 - Word Swap

import random


def main() -> None:
    print("Please input a sentence you wish to swap the words of:")
    sentence = input()
    swapSet = swapWords(sentence)
    swappedSetnence = dictToSentence(sentence, swapSet)
    print(swapSet)
    print(swappedSetnence)


def swapWords(s: str) -> dict:
    outDict = {}
    words = s.split()
    for w in words:
        outDict[w] = words[random.randint(0, len(words) - 1)]
    return outDict
        

def dictToSentence(s: str, d: dict) -> str:
    outStr = ""
    for w in s.split():
        outStr += f"{d.get(w)} "
    outStr.rstrip()
    return outStr



if __name__ == '__main__':
    main()