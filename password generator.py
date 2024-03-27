import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
    for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Please enter a valid positive integer.")
        except ValueError:
            print("Please enter a valid positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
