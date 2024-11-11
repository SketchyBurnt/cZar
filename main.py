def calculate_shift(password, shift):
    """
    Calculates the total shift based on the password and base shift value.
    """
    return shift + sum(ord(char) for char in password) % 26


def process_message(message, shift, operation):
    """
    Encodes or decodes a message by shifting characters. 
    `operation` can be 'encode' or 'decode'.
    """
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift_amount = shift if operation == 'encode' else -shift
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += new_char
        else:
            result += char  # Preserve non-alphabetic characters
    return result


def encode(message, password, shift):
    """
    Encodes a message using a password and shift value.
    """
    total_shift = calculate_shift(password, shift)
    return process_message(message, total_shift, 'encode')


def decode(encoded_message, password, shift):
    """
    Decodes a message using a password and shift value.
    """
    total_shift = calculate_shift(password, shift)
    return process_message(encoded_message, total_shift, 'decode')


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Select an option (1, 2, or 3): ").strip()

        if choice == '1':
            try:
                password = input("\nEnter the password for encoding: ").strip()
                message = input("Enter the message to encode: ").strip()
                shift = int(input("Enter the shift value: ").strip())
                disguised = encode(message, password, shift)
                print(f"\nDisguised Message: {disguised}")
            except ValueError:
                print("\nInvalid input. Please enter a valid number for the shift.")

        elif choice == '2':
            try:
                password = input("\nEnter the decoding password: ").strip()
                encoded_message = input("Enter the encoded message: ").strip()
                shift = int(input("Enter the shift value used for encoding: ").strip())
                decoded = decode(encoded_message, password, shift)
                print(f"\nDecoded Message: {decoded}")
            except ValueError:
                print("\nInvalid input. Please enter a valid number for the shift.")

        elif choice == '3':
            print("\nExiting...")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()