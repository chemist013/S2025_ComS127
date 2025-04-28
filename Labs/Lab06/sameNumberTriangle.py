# Joshua Hamaker        02/28/2025
# Lab06 - Same Number Triangle

def main():
    size = int(input("How large should the right triangle be? "))
    print("")
    sameNumberTriangle(size)

def sameNumberTriangle(s: int):
    for i in range(s):
        numOutput = str(i+1) + " "
        print(numOutput*(i+1))

if __name__ == "__main__":
    main()