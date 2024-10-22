def encode(message, password, shift):
    shift += sum([ord(char) for char in password]) % 26  # Calculate total shift
    encoded_message = ""

    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encoded_message += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encoded_message += chr(shifted)
        else:
            encoded_message += char  # Preserve non-alphabetic characters

    return encoded_message
