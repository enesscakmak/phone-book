def main():
    contacts = {}
    while True:
        print("1. Display contacts\n2.Search contact\n3.Add contact\n4.Exit")
        try:
            selection = int(input("Select the option you want to perform: "))
            if selection == 1:
                display_allcontact(contacts)
            elif selection == 2:
                searchcontact(contacts)
            elif selection == 3:
                addcontact(contacts)
            elif selection == 4:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")
        except Exception as e:
            print("An error occurred:", str(e))
    return contacts

def addcontact(contacts):
    try:
        name = input("Enter name: ")
        number=input("Enter number: ")
        contacts[name] = number
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("Success")

def searchcontact(contacts):
    name = input("Enter name: ")
    if name in contacts:
        print("Name: ", name, "\nNumber: ", contacts[name])
    else:
        print("Contact not found")

def display_allcontact(contacts):
    for name, number in contacts.items():
        print("Name: ", name, "\nNumber: ", number,"\n")


if __name__ == "__main__":
    contacts = main()