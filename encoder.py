import re
from utils import handle_double_letters

def encode(input_data):
 match = re.match(r"\((.*)\)\"(.*)\"\s*-(\d+)", input_data)
 if not match:
     print("\nInvalid syntax. Please try again.")
     return

 password = match.group(1)
 message = match.group(2)
 shift = int(match.group(3))

 shift += sum([ord(char) for char in password]) % 26
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
         encoded_message += char

 encoded_message = handle_double_letters(encoded_message)
 print(f"\nDisguised Message: {encoded_message}")
