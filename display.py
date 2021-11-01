import contacts

class Display:

    def __init__(self):
        self.contacts = contacts.Contacts()

    def __GetInfo(self):
        print ("please give me the name of the contact:\n"
               ">>")
        name = input()
        print ("Please give me the address of the contact:\n"
               ">>")
        address = input()
        print ("Please give the phone number of the contact:\n"
               ">>")
        phone = input()
        print ("please give the date of birth of the contact:\n"
               ">>")
        age = input()
        return (name, address, phone, age)

    def __AddContact(self):
        name, address, phone, age = self.__GetInfo()
        contact = self.contacts.ContactsAdd(name, address, phone, age)

    def __parse(self, choice):
        if choice.lower() == "list":
            self.contacts.ContactsList()
            return True
        if choice.lower() == "add":
            self.__AddContact()
            return True
        if choice.lower() == "remove":
            self.contacts.ContactsRemove()
            return True
        if choice.lower() == "edit":
            self.contacts.ContactsEdit()
            return True
        if choice.lower() == "search":
            self.contacts.ContactsSearch()
            return True
        if choice.lower() == "close":
            self.contacts.ContactsClose()
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
        print (intro)
        while start:
            print (menu)
            choice = input()
            start = self.__parse(choice)
