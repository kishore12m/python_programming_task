import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine the character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate password using random.choices()
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
