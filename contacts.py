class Contacts:
    def ContactsAdd(self, name, address, phone, age):
        f = open("Book.txt", "a")
        l = [name, address, phone, age]
        f.write(name + ", " + address + ", " + phone + ", " + age + "\n")
        f.close()
