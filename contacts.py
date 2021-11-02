class Contacts:
    def ContactsAdd(self, name, address, phone, age):
        f = open("Book.txt", "a")
        l = [name, address, phone, age]
        for elements in l:
            f.write(elements + "\n")


    def ContactsList(self):
        f = open("Book.txt","r")
        lineCount=0
        for line in f:
            if line !="\n":
                lineCount += 1
        lineGroup = int(lineCount/4)
        f.close()
        with open("Book.txt","r") as file:
            readline=file.read().split("\n")
            i = 0
            for x in range(0, lineGroup):
                print ('[{}, {}, {}, {}]'.format(readline[i], readline[i+1],
                                                  readline[i+2], readline[i+3]))
                i=i+4

    def ContactsRemove(self, name, address, phone, age):
        f = open("Book.txt","r")
        lineCount=0
        for line in f:
            if line !="\n":
                lineCount += 1
        lineGroup = int(lineCount/4)
        f.close()
        with open("Book.txt","r") as file:
            readline = file.read().split("\n")
            i = 0
            for x in range(0,lineGroup):
                if (readline[i].lower() == name.lower() and readline[i+1].lower() == address.lower()
                    and readline[i+2].lower() == phone.lower() and readline[i+3].lower() == age.lower()):
                    print ("Do you want to delete [{}, {}, {}, {}] Yes/No".format(name, address, phone, age))
                    ans= input()
                    if ans.lower() == "yes":
                        fl = open("Book.txt","w+")
                        a = i

                        del readline[a]
                        del readline[a]
                        del readline[a]
                        del readline[a]
                        for line in readline:
                            fl.write(line + "\n")
                        fl.close()
                        return True
                    if ans.lower() == "no":
                        print ("Cancelled Deletion")
                        return False
                else:
                    i = i+4
                    if i > lineCount:
                        return False



