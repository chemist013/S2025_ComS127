# Joshua Hamaker        02/28/2025
# Lab06 - Star Right Triangle

def main():
    size = int(input("How large should the right triangle be? "))
    print("")
    starRightTriangle(size)

def starRightTriangle(s: int):
    for i in range(s):
        print("* " * (i+1))

if __name__ == "__main__":
    main()