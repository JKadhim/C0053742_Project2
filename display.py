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



    def run(self):
        start = True
        intro = ("--Address-Book--\n"
                 "        ----------------")
        menu = """What would you like to do:
        >Add      | Adds a contact
        >List     | Lists all contacts
        >Remove   | Removes a contact
        >Edit     | Edits a contact
        >Search   | Searches for a specific contact
        >Close    | Ends the program"""
        print (intro)
        while start:
            print (menu)
            choice = input()
            start = self.__parse(choice)
