# Joshua Hamaker        04/01/2025
# Lecture Notes 04/01

## Exceptions
# I finally 'learn' try/except


# try:
#     answer = 12/0
# except Exception as e:
#     print(f"ERROR: {e}")
# print("Moving on...")


# try:
#     countries = []
#     countries.append("Denmark")
#     countries.append("Canada")
#     countries.append("Lazierstan")
#     print(countries[100])
# except Exception as e:
#     print(f"ERROR: {e}")
# print("Moving on...")


# class CustomException(Exception): # *inherits* from exception
#     pass


# def main() -> None:
#     try:
#         spam(2)
#     except CustomException as e:
#         print("ERROR", e)
#     else:
#         print("No errors")
#     finally:
#         print("The last thing")
#     print("</Program>")


# def spam(val) -> None:
#     if val % 2 == 0:
#         raise CustomException("spam() didn't work right")
#     print("Hello from spam()!")


# if __name__ == '__main__':
#     main()

while True:
    print("Please enter an intiger between 1-10:")
    val = input()
    try:
        val = int(val)
    except:
        print("ERROR: please enter an intiger")
        continue
    if val < 1 or val > 10:
        print("ERROR: value should be between 1 and 10")
        continue
    break

print(f"You entered {val}")
