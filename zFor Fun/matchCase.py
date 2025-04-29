x = int(input("x? "))

match x:
    case 1:
        print("x = 1")
    case 2:
        print("x = 2")
    case _:
        print("idk")

def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin

whats_on_the_telly(None)