address = {}
print "Welcome to the Address Book"
start = True
while start:
    user_choice = raw_input("Enter 'A' to Add, 'U' to Update, 'V' to View, 'D' to Delete, 'X' to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(address.keys()) < 1:
        print("Address book is empty right now")
      else:
        print address

    elif user_choice == "U":

      name = raw_input("Whats the name of the contact?")
      update = raw_input("Enter the new age of the contact:")
      address[update] = update
      print("Update was successful")
      print address

    elif user_choice == "A":
      name = raw_input("Enter name:")
      age = raw_input("Enter their age:")
      address.update = name
      print("The contact was successfully added")
      print address

    elif user_choice == "D":
      if len(address.keys()) < 1:
        print("Address book is empty")

      else:
        contact = raw_input("What contact?")
        for update in address.keys():
          if contact == name:
            del(address[update])
            print("The contact was successfully deleted")
            print address

          else:
            print("An incorrect contact was specified")

    elif user_choice == "X":
      start = False


