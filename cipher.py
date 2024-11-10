# add your code here
# make an array for uppercase and lowercase letters
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# receive message from user
message = input("Please enter the message you wish to encrypt:\n")

# store the caesar cypher shift key as a variable
SHIFT_KEY = 5

encrypted_message = "Result:\n"


for char in message:
    if char.isalpha():
        
        if char.isupper():
            working_alphabet = upper_alphabet

        else:
            working_alphabet = lower_alphabet

        char_index = working_alphabet.index(char)

        new_char_index = char_index + SHIFT_KEY

        if new_char_index > len(working_alphabet)-1:
            new_char_index -= len(working_alphabet)

        encrypted_message += working_alphabet[new_char_index]

    else:
        encrypted_message += char

print(encrypted_message)
