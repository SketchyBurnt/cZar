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
         input_data = input("\nEnter encoding syntax: (password)\"Message.\" -shift\n")
         encode(input_data)

     elif choice == '2':
         password = input("\nEnter the decoding password: ").strip()
         encoded_message = input("Enter the encoded message: ").strip()
         shift = int(input("Enter the shift used for encoding: ").strip())
         decode(encoded_message, password, shift)

     elif choice == '3':
         print("\nExiting...")
         break
     else:
         print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
 main_menu()
