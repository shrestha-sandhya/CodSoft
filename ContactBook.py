import os

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, old_phone_number, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.phone_number == old_phone_number:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, phone_number):
        for i, contact in enumerate(self.contacts):
            if contact.phone_number == phone_number:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        clear_console()

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            print("Contact List:")
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            print("Search Results:")
            contact_book.search_contact(query)

        elif choice == "4":
            old_phone_number = input("Enter the phone number of the contact to update: ")
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            updated_contact = Contact(name, phone_number, email, address)
            contact_book.update_contact(old_phone_number, updated_contact)

        elif choice == "5":
            phone_number = input("Enter the phone number of the contact to delete: ")
            contact_book.delete_contact(phone_number)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
