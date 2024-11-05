entries = {}

while True:
    options = ("exit", "list", "add", "update", "delete")
    choice = input("What would you like to do? Exit, List, Add or Delete? ").lower()
    if choice == "exit":
        break
    elif choice == "list":
        list()
    elif choice == "add":
        add()
    elif choice == "delete":
        delete()
    else:
        print("Invalid choice. Please try again.")

def list():

def add():


def delete():
