import random
import string

def generate_password():
    """Generates a random password based on user input."""
    
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        try:
            # Ask the user for the desired password length
            length = int(input("Enter desired password length (minimum 8): "))
            
            if length < 8:
                print("Password should be at least 8 characters long. Please try again.")
                continue
            
            # Generate the password using random.sample for uniqueness
            password = "".join(random.sample(characters, length))
            
            print(f"\nGenerated Password: {password}")
            break # Exit the loop if generation is successful
            
        except ValueError:
            print("Invalid input. Please enter a number.")
        except TypeError:
            # Handle potential issues if the character pool is less than the requested length
            print("Cannot generate a password of that length with available characters.")
            break

if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    generate_password()