# Joshua Hamaker        04/27/2025
# Lab 15 - Fizz Buzz


def main() -> None:
    print("Please enter an intiger:")
    while True:
        num = input()
        try:
            num = int(num)
            break
        except:
            print("Please enter an intiger:")
    print(fizzBuzzModulus(num))



def fizzBuzzModulus(n: int) -> str:
    fizz = n % 3 == 0
    buzz = n % 5 == 0
    bazz = n % 7 == 0
    if bazz:
        return "Bazz"
    elif fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return ""
    

if __name__ == '__main__':
    main()