def handle_double_letters(message):
 result = ""
 i = 0
 while i < len(message):
     result += message[i]
     if i > 0 and message[i] == message[i-1]:
         result = result[:-1] + 'x'
     i += 1
 return result
