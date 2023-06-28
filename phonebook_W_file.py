import os


file_path = os.path.join(os.getcwd(), "phoneBook/contacts.txt")

def main():
    while True:
        try:
            selection = int(input("Select the option you want to perform:\n1. Add a contact\n2. Search for a contact\n3. Display all contacts\n4. Exit\n"))
            if selection == 1:
                add_contact()
            elif selection == 2:
                search()
            elif selection == 3:
                display_contact()
            elif selection == 4:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")
        except Exception as e:
            print("An error occurred:", str(e))

def add_contact():
    phonebook = None
    try:
        os.makedirs("phonebook", exist_ok=True)
        phonebook = open(file_path, "a+", encoding="utf-8")
        name = input("Enter the name of the contact you want to add: ")
        phone = input("Enter the phone number of the contact: ")
        temp = name + " " + phone + "\n"
        phonebook.write(temp)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to access this file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if phonebook is not None:
            phonebook.close()

def search():
    phonebook = None
    try:
        os.makedirs("phonebook", exist_ok=True)
        phonebook = open(file_path, "r", encoding="utf-8")
        search = input("Enter the name of the contact you want to search for: ")
        for line in phonebook:
            if search in line:
                print(line, end="")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to access this file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if phonebook is not None:
            phonebook.close()

def display_contact():
    phonebook = None
    try:
        os.makedirs("phonebook", exist_ok=True)
        phonebook = open(file_path, "r", encoding="utf-8")
        for line in phonebook:
            print(line, end="")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to access this file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if phonebook is not None:
            phonebook.close()

main()
