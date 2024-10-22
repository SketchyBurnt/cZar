def decode(encoded_message, password, shift):
    shift += sum([ord(char) for char in password]) % 26  # Calculate total shift
    decoded_message = ""

    for char in encoded_message:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decoded_message += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decoded_message += chr(shifted)
        else:
            decoded_message += char  # Preserve non-alphabetic characters

    return decoded_message
