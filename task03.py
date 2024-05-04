import os

def load_contacts():
    contacts = {}
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone, email = line.strip().split(',')
                contacts[name] = {'phone': phone, 'email': email}
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"{name} has been added to your contacts.")

def view_contacts(contacts):
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print("Current information:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        contacts[name]['phone'] = input("Enter new phone number: ")
        contacts[name]['email'] = input("Enter new email address: ")
        save_contacts(contacts)
        print(f"{name}'s contact information has been updated.")
    else:
        print(f"{name} is not found in your contacts.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted from your contacts.")
    else:
        print(f"{name} is not found in your contacts.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nWelcome to the Contact Management System!")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()