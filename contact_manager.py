import json
import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"

    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for contact_data in data:
                    self.contacts.append(Contact(contact_data["name"], contact_data["phone"], contact_data["email"]))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.filename, "w") as f:
            data = [contact.__dict__ for contact in self.contacts]
            json.dump(data, f, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        while True:
            phone = input("Enter phone number (10 digits): ")
            # Validate phone number (10 digits only)
            if re.match(r"^\d{10}$", phone):
                break
            else:
                print("Invalid phone number. Please enter a 10-digit number.")

        while True:
            email = input("Enter email address (format: xyz@gmail.com): ")
            # Validate email format (basic check for @gmail.com)
            if re.match(r"^[a-zA-Z0-9_.+-]+@gmail\.com$", email):
                break
            else:
                print("Invalid email address. Please use the format xyz@gmail.com.")

        self.contacts.append(Contact(name, phone, email))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone} - {contact.email}")

    def edit_contact(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            self.view_contacts()
            index = int(input("Enter the contact index to edit: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                name = input("Enter new name (or press Enter to keep the same): ")
                while True:
                    phone = input("Enter new phone number (or press Enter to keep the same): ")
                    if not phone or re.match(r"^\d{10}$", phone):
                        break
                    else:
                        print("Invalid phone number. Please enter a 10-digit number or leave blank to keep existing.")
                while True:
                    email = input("Enter new email address (or press Enter to keep the same): ")
                    if not email or re.match(r"^[a-zA-Z0-9_.+-]+@gmail\.com$", email):
                        break
                    else:
                        print("Invalid email address. Please use the format xyz@gmail.com or leave blank to keep existing.")

                if name:
                    contact.name = name
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                print("Contact updated successfully!")
            else:
                print("Invalid contact index.")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            self.view_contacts()
            index = int(input("Enter the contact index to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                del self.contacts[index]
                print("Contact deleted successfully!")
            else:
                print("Invalid contact index.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            contact_manager.add_contact()
        elif choice == 2:
            contact_manager.view_contacts()
        elif choice == 3:
            contact_manager.edit_contact()
        elif choice == 4:
            contact_manager.delete_contact()
        elif choice == 5:
            contact_manager.save_contacts()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")