checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def printlist():
    print(checklist)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    list_all_items()


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index = index + 1


useritem = str()
command = str()
leavelist = 0


def addanitem():
    useritem = input("Add an item: ")
    useritem = str(useritem)
    create(useritem)


def checkofflist():
    useritem = input("type the name of the item you would like to check off?")
    useritem = str(useritem)
    for item in checklist:
        if useritem == item:
            pass
        else:
            print("we couldn't find your item on the list")
    for index in range(len(checklist)):
        if checklist[index] == useritem:
            checklist[index] = "√ " + checklist[index]
            print(checklist)


def takeitemoff():
    useritem = input("name the item you would like to take off the list.")
    useritem = str(useritem)
    for index in range(len(checklist)):
        if checklist[index] == useritem or checklist[index][2:len(checklist[index])] == useritem:
            destroy(index)
            print(checklist)
        else:
            print("we couldn't find your item on the list")


def runme():
    print("type add to add an item")
    print("type check to check off an item")
    print("type destroy to destroy an item")
    print("type exit to leave the list")
    print("type list to print your list")
    command = input()
    command = str(command).strip()
    if command == "add" or command == "Add":
        addanitem()
    elif command == "check" or command == "Check":
        checkofflist()
    elif command == "destroy" or command == "destroy":
        takeitemoff()
    elif command == "print" or command == "Print":
        printlist()
    elif command == "exit" or command == "Exit":
        global leavelist
        leavelist = leavelist + 1


while leavelist < 1:
    runme()
