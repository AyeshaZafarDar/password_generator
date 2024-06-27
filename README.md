# Random Password Generator

This is a Python script that generates a random password based on user-specified criteria, including length and character types (uppercase, lowercase, digits, and special characters).

## Features

- Allows user to specify the desired length of the password.
- Allows user to include/exclude uppercase letters, lowercase letters, digits, and special characters.
- Ensures at least one character from each selected type is included in the password.
- Validates user input to prevent errors and ensure a strong password.

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:

    ```bash
    python3 password_generator.py
    ```

4. Follow the prompts to enter the desired password length and choose the character types to include in the password.
5. The script will generate and display a random password based on your input.

## Example

```bash
$ python3 password_generator.py
Random Password Generator
Enter the desired password length: 8
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y
Generated Password: A7b@xY2#


## Code Explanation

### generate_password function

This function generates a random password with the given options.

- **Parameters:**
  - `length (int)`: Length of the password.
  - `use_uppercase (bool)`: Include uppercase letters.
  - `use_lowercase (bool)`: Include lowercase letters.
  - `use_digits (bool)`: Include digits.
  - `use_special (bool)`: Include special characters.
- **Returns:**
  - `str`: Generated password.

### main function

This function interacts with the user to get the desired password criteria and generates a password.

1. Prompts the user to enter the desired password length.
2. Prompts the user to specify whether to include uppercase letters, lowercase letters, digits, and special characters.
3. Validates the inputs and ensures at least one character type is selected.
4. Calls `generate_password` with the user's criteria and displays the generated password.

## Error Handling

- Ensures the password length is at least 4 if all character types are selected.
- Validates user inputs for password length and character type selections.
- Provides user-friendly error messages and prompts for re-entry of invalid inputs.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.