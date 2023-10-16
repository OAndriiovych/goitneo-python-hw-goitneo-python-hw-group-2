from typing import List, Dict, Tuple


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Add a contact to the contacts dictionary."""
    if len(args) != 2:
        return "Invalid format for adding contact. Use 'add [name] [phone]'."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Change the phone number of an existing contact."""
    if len(args) != 2:
        return "Invalid format for changing contact. Use 'change [name] [new phone]'."

    name, new_phone = args
    if name not in contacts:
        return f"No contact found for name: {name}."

    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Show the phone number for a given contact name."""
    if not args:
        return "Invalid format for showing phone. Use 'phone [name]'."

    name = args[0]
    return contacts.get(name, f"No contact found for name: {name}.")


def show_all(contacts: Dict[str, str]) -> str:
    """Show all saved contacts and their phone numbers."""
    if not contacts:
        return "No contacts saved."

    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Parse the user input to extract command and arguments."""
    cmd, *args = user_input.strip().lower().split()
    return cmd, args


def main():
    """Main function for the bot assistant."""
    print("Welcome to the assistant bot!")
    contacts = {}

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")