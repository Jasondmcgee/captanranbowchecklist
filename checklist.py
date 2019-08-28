checklist = list()

# CREATE
def create(item):
    # Create item code here

# READ
def read(index):
    # Read code here

# UPDATE
def update(index, item):
    # Update code here

# DESTROY
def destroy(index):


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
