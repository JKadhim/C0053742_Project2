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
            readLine = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # formats the txt file into each contact and prints them
                print('[{}, {}, {}, {}]'.format(readLine[i], readLine[i + 1],
                                                readLine[i + 2], readLine[i + 3]))
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
            readLine = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # searches the file for the specified file
                if (readLine[i].lower() == name.lower() and readLine[i + 1].lower() == address.lower()
                        and readLine[i + 2].lower() == phone.lower() and readLine[i + 3].lower() == age.lower()):
                    print("Do you want to delete [{}, {}, {}, {}] Yes/No".format(name, address, phone, age))
                    ans = input()  # extra layer of checking
                    if ans.lower() == "yes":
                        fl = open("Book.txt", "w+")
                        a = i

                        del readLine[a]  # removes all attributes of the contact
                        del readLine[a]
                        del readLine[a]
                        del readLine[a]
                        for line in readLine:
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
            readLine = file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):  # searches the file for the specified file
                if (readLine[i].lower() == name.lower() and readLine[i + 1].lower() == address.lower()
                        and readLine[i + 2].lower() == phone.lower() and readLine[i + 3].lower() == age.lower()):
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
                        lineReader = open("Book.txt", "r")
                        lineList = lineReader.readlines()  # creates a list of the text file
                        lineList[i] = (name + "\n")  # replaces the line with the new information x4
                        lineList[i + 1] = (address + "\n")
                        lineList[i + 2] = (phone + "\n")
                        lineList[i + 3] = (age + "\n")
                        lineReader = open("Book.txt", "w")
                        lineReader.writelines(lineList)  # replaces the whole file with the new data
                        lineReader.close()
                        return True
                    else:
                        return False  # cancels the action if the user chooses to
                else:
                    print("--User-Not-Found--")
                    return False  # cancels if the contact doesnt exist

    def ContactsSearch(self):
        f = open("Book.txt", "r")
        lineCount = 0
        for line in f:  # counts the number of lines in the txt file
            if line != "\n":
                lineCount += 1
        lineGroup = int(lineCount / 4)  # splits the lines into each contact
        f.close()
        with open("Book.txt", "r") as file:
            lineList = file.read().split("\n")  # Creates an array of he text file without the \n
            print("""What would you like to search for?:
            >Name
            >Address
            >Number
            >DOB""")
            searchChoice = input(">>")
            if searchChoice.lower() == "name":  # searches using the name of the contact
                search = input("What name are you searching for?")
                i = 0
                c = 0
                print("--List-Of-Matches--")
                for x in range(0, lineGroup):
                    if search.lower() == lineList[i]:  # prints out if there is a match
                        print("[{}, {}, {}, {}]".format(lineList[i], lineList[i + 1], lineList[i + 2], lineList[i + 3]))
                        c = c + 1  # changes if there are any matches
                    i = i + 4
                if c == 0:  # if there are no matches
                    print("--No-Matches--")
                    return False
                else:
                    return True

            elif searchChoice.lower() == "address":  # searches using address of contact
                search = input("What address are you searching for?")
                i = 0
                c = 0
                print("--List-Of-Matches--")
                for x in range(0, lineGroup):
                    if search.lower() == lineList[i + 1]:  # prints if there is a match
                        print("[{}, {}, {}, {}]".format(lineList[i], lineList[i + 1], lineList[i + 2], lineList[i + 3]))
                        c = c + 1  # changes if there is a match
                    i = i + 4
                if c == 0:  # prints if there isn't a match
                    print("--No-Matches--")
                    return False
                else:
                    return True

            elif searchChoice.lower() == "number":  # searches using the number of the contact
                search = input("What phone number are you searching for?")
                i = 0
                c = 0
                print("--List-Of-Matches--")
                for x in range(0, lineGroup):
                    if search.lower() == lineList[i + 2]:  # prints if there is a match
                        print("[{}, {}, {}, {}]".format(lineList[i], lineList[i + 1], lineList[i + 2], lineList[i + 3]))
                        c = c + 1  # changes if there is a match
                    i = i + 4
                if c == 0:  # prints if there isn't a match
                    print("--No-Matches--")
                    return False
                else:
                    return True

            elif searchChoice.lower() == "birthday":  # searches using the birthday of the contact
                search = input("What Birthday are you searching for?")
                i = 0
                c = 0
                print("--List-Of-Matches--")
                for x in range(0, lineGroup):
                    if search.lower() == lineList[i + 3]:  # prints if there is a match
                        print("[{}, {}, {}, {}]".format(lineList[i], lineList[i + 1], lineList[i + 2], lineList[i + 3]))
                        c = c + 1  # changes if there is a match
                    i = i + 4
                if c == 0:  # prints if there isn't a match
                    print("--No-Matches--")
                    return False
                else:
                    return True

            else:  # runs if the input is invalid
                print("--Invalid-Input--")
                return False
