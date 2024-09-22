class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter the contact name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        address = input("Enter the address: ")
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ")
        found = False
        for name, details in self.contacts.items():
            if name == search_term or details['phone'] == search_term:
                print(f"Found: Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            print("Current details:", self.contacts[name])
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

    def menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
