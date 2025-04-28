# Joshua Hamaker        04/03/2025
# Lab 11 - Remove non-ASCII chars


def main() -> None:
    print("Please enter the name of the file to be scrubbed of ASCII characters:")
    fileName = input()
    fileContents = fileToStr(fileName)
    # print(fileContents)
    cleanFileContents = removeNonASCII(fileContents)
    newFileName = f"{fileName.replace(".txt", "")}_clean.txt"
    # print(newFileName)
    with open(newFileName, "w") as f:
        f.write(cleanFileContents)


def fileToStr(name: str) -> str:
    with open(name, "r", encoding="UTF-8") as f:
        outStr = f.read()
    return outStr


def removeNonASCII(text: str) -> str:
    clean = ""
    for i in text:
        if ord(i) <= 127:
            clean += i
    return clean


if __name__ == '__main__':
    main() 