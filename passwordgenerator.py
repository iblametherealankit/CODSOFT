import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''

    # Combine all chosen character sets
    all_characters = lowercase + uppercase + digits + special_characters

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # User input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (min 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Ask user about complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)

    # Display the password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
