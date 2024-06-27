"""
This module provides functionality to generate a random password based on user-specified criteria.
It includes options to use uppercase letters, lowercase letters, digits, and special characters.
"""
import string
import random

# Function to generate a random password with the given options
def generate_password(length, use_uppercase=True, use_lowercase=True, \
                      use_digits=True, use_special=True):
    """
    Generate a random password with the given options.
    
    Parameters:
    - length (int): Length of the password
    - use_uppercase (bool): Include uppercase letters
    - use_lowercase (bool): Include lowercase letters
    - use_digits (bool): Include digits
    - use_special (bool): Include special characters
    
    Returns:
    - str: Generated password
    
    Raises:
    - ValueError: If length is less than 4 when all character types are selected
    """
    # Check if all character types are selected and length is less than 4
    if length < 4 and (use_uppercase and use_lowercase and use_digits and use_special):
        raise ValueError("Password length must be at least 4 when all character types are selected")
    # Initialize an empty list to collect characters for the password
    password = []
    # Add one character from each selected type to the password list
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    # Calculate the remaining length needed to reach the desired password length
    remaining_length = length - len(password)
    # Build a pool of characters from all selected types
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    # Add random characters from the pool to the password list until the desired length is reached
    if remaining_length > 0:
        password.extend(random.choice(character_pool) for _ in range(remaining_length))
    # Shuffle the password list to ensure random order
    random.shuffle(password)
    # Convert the password list to a string and return it
    return ''.join(password)

# Main function to interact with the user and generate a password based on their input
def main():
    """
    Main function to interact with the user and generate a password based on their input.
    
    Prompts the user for password length and character type options, then generates and
    displays a random password based on the provided criteria.
    """
    print("Random Password Generator")
    # Loop to get a valid password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                raise ValueError("Password length must be at least 4")
            break
        except ValueError as ve:
            print(f"Invalid input for password length: {ve}")
    # Loop to get valid character type selections from the user
    while True:
        use_uppercase = input("Include uppercase letters? (y/n): ").lower()
        use_lowercase = input("Include lowercase letters? (y/n): ").lower()
        use_digits = input("Include digits? (y/n): ").lower()
        use_special = input("Include special characters? (y/n): ").lower()
        # Validate the input for character type selections
        if use_uppercase not in ['y', 'n'] or use_lowercase not in ['y', 'n'] or \
            use_digits not in ['y', 'n'] or use_special not in ['y', 'n']:
            print("Please enter 'y' or 'n' for each option.")
            continue
        # Convert inputs to boolean values
        use_uppercase = use_uppercase == 'y'
        use_lowercase = use_lowercase == 'y'
        use_digits = use_digits == 'y'
        use_special = use_special == 'y'
        # Ensure at least one character type is selected
        if not any([use_uppercase, use_lowercase, use_digits, use_special]):
            print("At least one type of character must be selected")
            continue
        # Try generating the password with the given options
        try:
            password = generate_password(length, use_uppercase, use_lowercase, \
                                         use_digits, use_special)
            print("Generated Password:", password)
            break
        except ValueError as ve:
            print(f"Error generating password: {ve}")

# Entry point of the script
if __name__ == "__main__":
    main()
