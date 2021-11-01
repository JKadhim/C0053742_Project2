import address


def main():
    print("""----Address Book----
    --------------------""")
    loop1 = True
    while loop1:
        try:
            setting = int(input("What would you like to do?:\n"
                                "1: Add a new contact\n"
                                "2: Alter an existing contact\n"
                                "3: View a contact\n"
                                "4: Delete a contact\n"
                                "5: Exit application\n"
                                ">>"))
            if setting > 5 or setting < 1:
                print("--You must input an integer within range")
        except ValueError:
            print("--You must input an integer--")
        if setting == 1:
            add()

def add():
    name= str(input("Enter the contacts name:"))
    address= str(input("Enter the contacts address:"))
    phone= str(input("enter the contacts phone number:"))
    birth= str(input("enter the contacts birthday(DD/MM/YYYY):"))



