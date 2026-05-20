
def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():  # Check if character is a letter
            # Convert character to uppercase
            char = char.upper()

            # Shift the character
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += new_char
        else:
            # Preserve spaces and other characters
            encrypted_message += char

    return encrypted_message


# Function to decrypt the message
def decrypt(message, shift):
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            char = char.upper()

            # Reverse the shift
            new_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_message += new_char
        else:
            decrypted_message += char

    return decrypted_message


# Main program
print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option (1 or 2): ")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    result = encrypt(message, shift)
    print("Encrypted message:", result)

elif choice == "2":
    result = decrypt(message, shift)
    print("Decrypted message:", result)

else:
    print("Invalid choice!")