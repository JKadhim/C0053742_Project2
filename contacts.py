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
