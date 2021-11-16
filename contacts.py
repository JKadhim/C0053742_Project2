class Contacts:
    def ContactsAdd(self, name, address, phone, age):
        f = open("Book.txt", "a")  # opens in append mode
        l = [name, address, phone, age]
        for elements in l:
            f.write(elements + "\n")  # adds the elements to the file

    def ContactsList(self):
        f = open("Book.txt", "r")
        lineCount = 0
        for line in f:  # counts the number of lines in the txt file
            if line != "\n":
                lineCount += 1
        lineGroup = int(lineCount / 4)  # splits the lines into each contact
        f.close()
        with open("Book.txt", "r") as file:
            readline = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # formats the txt file into each contact and prints them
                print('[{}, {}, {}, {}]'.format(readline[i], readline[i + 1],
                                                readline[i + 2], readline[i + 3]))
                i = i + 4

    def ContactsRemove(self, name, address, phone, age):
        f = open("Book.txt", "r")
        lineCount = 0
        for line in f:  # counts the number of lines in the txt file
            if line != "\n":
                lineCount += 1
        lineGroup = int(lineCount / 4)  # splits the lines into each contact
        f.close()
        with open("Book.txt", "r") as file:
            readline = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # searches the file for the specified file
                if (readline[i].lower() == name.lower() and readline[i + 1].lower() == address.lower()
                        and readline[i + 2].lower() == phone.lower() and readline[i + 3].lower() == age.lower()):
                    print("Do you want to delete [{}, {}, {}, {}] Yes/No".format(name, address, phone, age))
                    ans = input()  # extra layer of checking
                    if ans.lower() == "yes":
                        fl = open("Book.txt", "w+")
                        a = i

                        del readline[a]  # removes all attributes of the contact
                        del readline[a]
                        del readline[a]
                        del readline[a]
                        for line in readline:
                            fl.write(line + "\n")
                        fl.close()
                        return True
                    if ans.lower() == "no":
                        print("Cancelled Deletion")
                        return False  # stops the deletion process
                else:  # check the next contact for a match
                    i = i + 4
                    if i > lineCount:  # checks if the search is out of range
                        return False

    def ContactsEdit(self, name, address, phone, age):
        f = open("Book.txt", "r")
        lineCount = 0
        for line in f:  # counts the number of lines in the txt file
            if line != "\n":
                lineCount += 1
        lineGroup = int(lineCount / 4)  # splits the lines into each contact
        f.close()
        with open("Book.txt", "r") as file:
            readline = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # searches the file for the specified file
                if (readline[i].lower() == name.lower() and readline[i + 1].lower() == address.lower()
                        and readline[i + 2].lower() == phone.lower() and readline[i + 3].lower() == age.lower()):
                    print("Do you want to edit [{}, {}, {}, {}] Yes/No".format(name, address, phone, age))
                    ans = input()  # extra layer of checking
                    if ans.lower() == "yes":
                        print("--Edit-Contact--")
                        print("please give me the name of the contact:\n"
                              ">>")
                        name = input()  # asks for the edited name
                        print("Please give me the address of the contact:\n"
                              ">>")
                        address = input()  # asks for the edited address
                        print("Please give the phone number of the contact:\n"
                              ">>")
                        phone = input()  # asks for the edited phone number
                        print("please give the date of birth of the contact:\n"
                              ">>")  # asks for the edited date of birth
                        age = input()
                        linereader = open("Book.txt", "r")
                        linelist = linereader.readlines()  # creates a list of the text file
                        linelist[i] = (name + "\n")  # replaces the line with the new information x4
                        linelist[i + 1] = (address + "\n")
                        linelist[i + 2] = (phone + "\n")
                        linelist[i + 3] = (age + "\n")
                        linereader = open("Book.txt", "w")
                        linereader.writelines(linelist)  # replaces the whole file with the new data
                        linereader.close()
                        return True
                    else:
                        return False  # cancels the action if the user chooses to
                else:
                    print("--User-Not-Found--")
                    return False  # cancels if the contact doesnt exist

    def ContactsSearch(self, name, address, phone, age):
