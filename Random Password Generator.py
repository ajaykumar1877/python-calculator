import random
import string

def generate_password():
    """
    Generates a random password based on user-specified length.
    Includes letters, digits, and special characters.
    """
    try:
        # Ask the user for desired password length
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return

        # Characters to include in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"Generated Password ({length} characters): {password}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Call the function
generate_password()
