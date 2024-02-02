# This function takes a text and a shift value and returns the encrypted text.
def encrypt(text, shift):
    result = ""  # Initialize an empty string to store the encrypted text.
    
    for char in text:  # Loop through each character in the input text.
        if char.isalnum():  # Check if the character is alphanumeric (letter or number).
            if char.isalpha():  # Check if the character is an alphabet letter.
                if char.isupper():  # Check if the letter is uppercase.
                    # Shift the uppercase letter and add it to the result.
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    # Shift the lowercase letter and add it to the result.
                    result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                # Shift the number and add it to the result.
                result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            # If the character is not alphanumeric, keep it unchanged.
            result += char
    
    # Return the final encrypted text.
    return result

# This function takes a text and a shift value and returns the decrypted text.
def decrypt(text, shift):
    # Use the encrypt function with a negative shift to decrypt the text.
    return encrypt(text, -shift)

# This is the main function where the program starts.
def main():
    # Ask the user to enter the text they want to encrypt.
    text = input("Enter the text to encrypt: ")
    # Ask the user to enter the shift value (the secret key).
    shift = int(input("Enter the shift value: "))
    
    # Call the encrypt function to get the encrypted text.
    encrypted_text = encrypt(text, shift)
    # Call the decrypt function to get the decrypted text.
    decrypted_text = decrypt(encrypted_text, shift)
    
    # Display the encrypted and decrypted texts.
    print("\nEncrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

# Check if the script is being run directly (not imported as a module).
if __name__ == "__main__":
    # Call the main function to start the program.
    main()
