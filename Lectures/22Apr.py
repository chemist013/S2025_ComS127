# Joshua Hamaker        04/22/2025
# Lectrue Notes 04/22

## Recursion
    # A function calling itself


def countUp(n: int) -> None:
    if n <= 0:
        return
    countUp(n - 1)
    print(n)


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def pell(n: int) -> int:
    if n < 0:
        return -1
    elif n <= 1:
        return n
    return 2 * pell(n - 1) + pell(n - 2)


def main() -> None:
    # countUp(5)
    print(factorial(5)) # 120
    print(fibonacci(7)) # 13
    print(pell(5)) # 29


if __name__ == '__main__':
    main()