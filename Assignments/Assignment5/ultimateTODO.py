# Joshua Hamaker            04/07/2025
# Assignment 5 - Ultimate ToDo List
# This program is a tool for organization of a user's tasks

import sys
import pickle


def printTitleMaterial() -> None:
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()
    print("By: Joshua Hamaker")
    print("[COM S 127 1]")
    print()


def initList() -> dict[str, list]:
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []
    return todoList


def checkIfListEmpty(todoList: dict[str, list]) -> bool:
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True


def saveList(todoList: dict[str, list]) -> None:
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()


def loadList() -> dict[str, list]:
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    return todoList


def checkItem(item: str, todoList: dict[str, list]) -> tuple[bool, str, int]:
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1
    for k in todoList.keys():
        for v in todoList[k]:
            if v == item:
                itemFound = True
                keyName = k
                index = todoList[k].index(v)
                return itemFound, keyName, index
    return itemFound, keyName, index


def addItem(item: str, toList: str, todoList: dict[str, list]) -> dict[str, list]:
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == True:
        print(f"ERROR: {item} already exists")
        print(f"Location: list -> {keyName} @ index -> {index}")
    else:
        todoList[toList].append(item)
    return todoList


def deleteItem(item: str, todoList: dict[str, list]) -> tuple[bool, dict[str, list]]:
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == False:
        print(f"ERROR: {item} not found in any list")
    else:
        del todoList[keyName][index]
    return itemFound, todoList


def moveItem(item: str, toList: str, todoList: dict[str, list]) -> dict[str, list]:
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    deleteSuccess, todoList = deleteItem(item, todoList)
    if deleteSuccess == True:
        todoList = addItem(item, toList, todoList)
    return todoList


def printTODOList(todoList: dict[str, list]) -> None:
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    for k in todoList.keys():
        print(f"{k}: {todoList[k]}")
    return None


def runApplication(todoList: dict[str, list]) -> dict[str, list]:
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            print("Please enter a task:")
            task = input()
            todoList = addItem(task, "backlog", todoList)
            printTODOList(todoList)
        elif choice == "m":
            listEmpty = checkIfListEmpty(todoList)
            if not listEmpty:
                while True:
                    print("Please enter the task to be moved:")
                    taskToMove = input()
                    itemExists, keyName, index = checkItem(taskToMove, todoList)
                    if itemExists:
                        break
                    print(f"{taskToMove} does not exist")
                while True:
                    print(f"Please enter where {taskToMove} should be moved:")
                    moveLocation = input()
                    if moveLocation in todoList.keys():
                        break
                    print(f"{moveLocation} is not a valid list name")
                todoList = moveItem(taskToMove, moveLocation, todoList)
                print()
            else:
                print("ERROR: No items to move\nPlease add an item to a list first with [a]")
                print()
            printTODOList(todoList)
        elif choice == "d":
            listEmpty = checkIfListEmpty(todoList)
            if not listEmpty:
                print("Please enter the task to be deleted:")
                taskToDelete = input()
                itemExists, todoList = deleteItem(taskToDelete, todoList)
                print()
            else:
                print("ERROR: No items to delete\nPlease add an item to a list first with [a]")
                print()
            printTODOList(todoList)
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList


def main() -> None:
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()


if __name__ == "__main__":
    main()