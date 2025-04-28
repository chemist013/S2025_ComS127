# Joshua Hamaker        02/28/2025
# Lab06 - Number Diamond

def main():
    size = int(input("How large should the diamond be? "))
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
    for i in range(s,0,-1):
        padding = int(totLen - (i-1))
        currentStr = " "*padding + oldStr.replace(str(i),"")
        print(currentStr)
        oldStr = currentStr.strip() + " "

if __name__ == "__main__":
    main()