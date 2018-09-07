address = []
start = 1

def mainMenu():
    while start == 1:
        choice = input("Enter '1' to Add, '2' to View, '3' to End Program \n")
        if choice == "1":
            add()

        elif choice == "2":
            view()

        elif choice == "3":
            stop()

        else:
            print ("invalid")


def add():
    global name
    name = input("Enter name:")
    age =  input("Enter their age:")
    phone = input("Enter their phone number:")
    address.append("Name: "+ name + ", Age: " + age + ", Phone number: " + phone)
    print("The contact was successfully added")
    print (address)
    mainMenu()

def view():
    print (address)

def stop():
    global start
    start = 0


mainMenu()

