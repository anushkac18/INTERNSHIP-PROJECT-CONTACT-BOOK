import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

# Search for a contact
def search_contact(contacts):
    query = input("Search by name or phone: ").lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    if results:
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact}")
    else:
        print("No contacts found.")

# Update a contact
def update_contact(contacts):
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input(f"New phone (current: {contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"New email (current: {contact['email']}): ") or contact["email"]
            print("Contact updated.")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            contacts.pop(i)
            print("Contact deleted.")
            return
    print("Contact not found.")

# Menu loop
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            for contact in contacts:
                print(contact)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
