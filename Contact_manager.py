class ContactManager:
    def __init__(self):
        self.contacts = []

    def display_menu(self):
        """Display the main menu."""
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def add_contact(self):
        """Add a new contact."""
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        address = input("Enter address: ").strip()

        if name and phone:
            self.contacts.append({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            print(f"Contact '{name}' added successfully!")
        else:
            print("Name and phone number are required to add a contact.")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} | {contact['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        query = input("Enter name or phone number to search: ").strip()
        results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]

        if results:
            print("\nSearch Results:")
            for contact in results:
                self.display_contact(contact)
        else:
            print("No matching contact found.")

    def update_contact(self):
        """Update contact details."""
        self.view_contacts()
        try:
            contact_number = int(input("Enter the contact number to update: "))
            if 1 <= contact_number <= len(self.contacts):
                contact = self.contacts[contact_number - 1]
                print("Enter new details (leave blank to keep unchanged):")
                name = input(f"Name [{contact['name']}]: ").strip() or contact['name']
                phone = input(f"Phone [{contact['phone']}]: ").strip() or contact['phone']
                email = input(f"Email [{contact['email']}]: ").strip() or contact['email']
                address = input(f"Address [{contact['address']}]: ").strip() or contact['address']

                contact.update({"name": name, "phone": phone, "email": email, "address": address})
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_contact(self):
        """Delete a contact."""
        self.view_contacts()
        try:
            contact_number = int(input("Enter the contact number to delete: "))
            if 1 <= contact_number <= len(self.contacts):
                removed_contact = self.contacts.pop(contact_number - 1)
                print(f"Contact '{removed_contact['name']}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

    def display_contact(self, contact):
        """Display detailed contact information."""
        print("\nContact Details:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    def run(self):
        """Main method to run the contact manager."""
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-6): "))
                if choice == 1:
                    self.add_contact()
                elif choice == 2:
                    self.view_contacts()
                elif choice == 3:
                    self.search_contact()
                elif choice == 4:
                    self.update_contact()
                elif choice == 5:
                    self.delete_contact()
                elif choice == 6:
                    print("Exiting Contact Manager. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a valid number.")

# Run the Contact Manager application
if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
