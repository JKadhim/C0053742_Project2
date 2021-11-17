import contacts


class Display:

    def __init__(self):
        self.contacts = contacts.Contacts()

    def __GetInfo(self):
        print("please give me the name of the contact:\n"
              ">>")
        name = input()
        print("Please give me the address of the contact:\n"
              ">>")
        address = input()
        print("Please give the phone number of the contact:\n"
              ">>")
        phone = input()
        print("please give the date of birth of the contact:\n"
              ">>")
        age = input()
        return name, address, phone, age  # gets all necessary info for the address book

    def __AddContact(self):
        name, address, phone, age = self.__GetInfo()  # gets info from the user
        contact = self.contacts.ContactsAdd(name, address, phone, age)  # adds the info to the txt file

    def __RemoveContact(self):
        name, address, phone, age = self.__GetInfo()  # gets info from the user
        if self.contacts.ContactsRemove(name, address, phone, age):  # checks then removes the contact
            print("--Contact-Deleted--")
        else:
            print("--Failed-To-Delete--")

    def __EditContact(self):
        print("Enter the details of the user you want to edit")
        name, address, phone, age = self.__GetInfo()
        if self.contacts.ContactsEdit(name, address, phone, age):
            print("--Contact-Edited--")  # if the method is successful
        else:
            print("--Failed-To-Edit--")  # if the method is unsuccessful

    def __SearchContact(self):
        if self.contacts.ContactsSearch():  # if there are valid contacts
            print("--End-of-list--")
        else:  # if exited or there isn't a valid contact
            print("--No-Valid-Contact--")

    def __parse(self, choice):
        if choice.lower() == "list":  # lists the contacts in the txt file
            self.contacts.ContactsList()
            return True
        if choice.lower() == "add":  # adds a contact to the txt file
            self.__AddContact()
            return True
        if choice.lower() == "remove":
            self.__RemoveContact()  # removes a contact from the txt file
            return True
        if choice.lower() == "edit":  # alters a contact in the txt file
            self.__EditContact()
            return True
        if choice.lower() == "search":  # searches for an existing contact
            self.__SearchContact()
            return True
        if choice.lower() == "close":  # Ends the program
            print("--End-Of-Program--")
            return False
        else:  # returns to the menu
            print("--Invalid-Choice--")
            return True

    def run(self):
        start = True
        intro = ("--Address-Book--\n"
                 "        ----------------")
        menu = ("What would you like to do:\n"
                ">Add      | Adds a contact\n"
                ">List     | Lists all contacts\n"
                ">Remove   | Removes a contact\n"
                ">Edit     | Edits a contact\n"
                ">Search   | Searches for a specific contact\n"
                ">Close    | Ends the program\n"
                ">>")
        print(intro)
        while start:
            print(menu)  # prints out the UI
            choice = input()
            begin = self.__parse(choice)  # sends choice to __parse
