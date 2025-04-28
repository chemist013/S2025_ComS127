# Joshua Hamaker        04/04/2025
# Lab 11 - Book Analysis


def main() -> None:
    print("Please enter the name of the file containing the book to be analyzed:")
    fileName = input()
    countDict = analyzeBook(fileName)
    outputAnalysis(fileName, countDict)


def analyzeBook(file: str) -> dict:
    outDict = {}
    with open(file, "r") as f:
        for l in f:
            for w in l.split():
                w = w.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                w = w.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                w = w.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                w = w.replace(']', '').replace(';', '')
                w = w.lower()
                if w.isalpha():
                    if w in outDict:
                        outDict[w] += 1
                    else:
                        outDict[w] = 1
    return outDict


def outputAnalysis(file: str, count: dict) -> None:
    keys = list(count.keys())
    keys.sort()
    newFileName = f"{file.replace(".txt", "")}_words.txt"
    with open(newFileName, "w") as f:
        for w in keys:
            f.write(f"{w} {str(count[w])}\n")


if __name__ == '__main__':
    main()