# Dictionary-Based Phonebook Project

# Initial phonebook dictionary
phonebook = {
    "Amit": "9876543210",
    "Riya": "9123456780"
}

# Function to add a new contact
def add_contact(name, number):
    if name in phonebook:
        print(f"{name} already exists! Duplicate entry not allowed.")
    else:
        phonebook[name] = number
        print(f"Contact {name} added successfully.")

# Function to search a contact by exact name
def search_contact(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

# Function to search contact by partial name
def partial_search(partial):
    found = False
    for name, number in phonebook.items():
        if partial.lower() in name.lower():
            print(f"{name}: {number}")
            found = True
    if not found:
        print(f"No contacts found with '{partial}'.")

# Function to delete a contact
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"{name} not found in phonebook.")

# Function to display all contacts
def display_contacts():
    if phonebook:
        print("\n--- Phonebook Contacts ---")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# Main program loop
while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Partial Search")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        partial = input("Enter partial name: ")
        partial_search(partial)

    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Exiting Phonebook. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")