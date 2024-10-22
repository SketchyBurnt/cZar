from encoder import encode
from decoder import decode

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Select an option (1, 2, or 3): ").strip()

        if choice == '1':
            # Encoding process
            password = input("\nEnter the password for encoding: ").strip()
            message = input("Enter the message to encode: ").strip()
            shift = int(input("Enter the shift value: ").strip())
            disguised = encode(message, password, shift)
            print(f"\nDisguised Message: {disguised}")

        elif choice == '2':
            # Decoding process
            password = input("\nEnter the decoding password: ").strip()
            encoded_message = input("Enter the encoded message: ").strip()
            shift = int(input("Enter the shift value used for encoding: ").strip())
            decoded = decode(encoded_message, password, shift)
            print(f"\nDecoded Message: {decoded}")

        elif choice == '3':
            print("\nExiting...")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
