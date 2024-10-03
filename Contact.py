# Step 1: Define a class to manage contacts
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Step 2: Define a class to handle the contact management operations
class ContactManager:
    def __init__(self):
        self.contacts = []  # List to store all contacts
    
    # Add a new contact
    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully.")
    
    # View the contact list
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")
    
    # Search contact by name or phone number
    def search_contact(self):
        query = input("\nEnter name or phone number to search: ").lower()
        found_contacts = [c for c in self.contacts if query in c.name.lower() or query in c.phone]
        
        if found_contacts:
            print("\n--- Search Results ---")
            for contact in found_contacts:
                self.display_contact_details(contact)
        else:
            print(f"\nNo contact found with '{query}'.")

    # Update a contact's details
    def update_contact(self):
        self.view_contacts()
        choice = int(input("\nEnter the number of the contact you want to update: ")) - 1
        
        if 0 <= choice < len(self.contacts):
            contact = self.contacts[choice]
            print("\n--- Update Contact Details ---")
            contact.name = input(f"Enter new name ({contact.name}): ") or contact.name
            contact.phone = input(f"Enter new phone number ({contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
            contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
            print(f"\nContact '{contact.name}' updated successfully.")
        else:
            print("\nInvalid selection.")
    
    # Delete a contact
    def delete_contact(self):
        self.view_contacts()
        choice = int(input("\nEnter the number of the contact you want to delete: ")) - 1
        
        if 0 <= choice < len(self.contacts):
            contact = self.contacts.pop(choice)
            print(f"\nContact '{contact.name}' deleted successfully.")
        else:
            print("\nInvalid selection.")
    
    # Display full contact details
    def display_contact_details(self, contact):
        print(f"\nName: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

# Step 3: Create a function for the user-friendly interface
def display_menu():
    print("\n--- Contact Manager ---")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Step 4: Main loop for user interaction
def main():
    manager = ContactManager()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("\nExiting Contact Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Start the program
main()
