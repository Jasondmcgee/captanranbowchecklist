checklist = list()

# CREATE
def create(item):
    # Create item code here
    checklist.append(item)

# READ
def read(index):
    # Read code here
    return checklist[index]


# UPDATE
def update(index, item):
    # Update code here
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)


def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))


test()
