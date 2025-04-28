# Joshua Hamaker        02/28/2025
# Lab06 - Number Pyramid

def main():
    size = int(input("How large should the pyramid be? "))
    print("")
    numberPyramid(size)

def numberPyramid(s):
    totLen = 2*s-1
    oldStr = ""
    for i in range(s):
        padding = int(totLen - (i+1))
        currentStr = " "*padding + oldStr + str(i+1) + " "
        print(currentStr)
        oldStr = currentStr.strip() + " "

if __name__ == "__main__":
    main()