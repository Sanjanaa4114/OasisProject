import string
import random

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!🔐 ")
    try:
        length = int(input("Enter desired password length: "))

        print("\nInclude character types:")
        use_letters = input("Letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print(" Please enter a valid number for password length.")

if __name__ == "__main__":
    main()