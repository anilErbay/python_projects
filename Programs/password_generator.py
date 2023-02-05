import random


def generate_password():
    print(" *******  PASSWORD GENERATOR  *******")
    toggle = True
    while toggle:
        try:
            password_length = int(input("Enter the length of the password: "))
            chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            password = "".join(random.sample(chars, password_length))
            toggle = False
        except ValueError as e:
            print("Invalid input. Please try again...")
            print(e)
        else:
            print()
            print(f"Generated Password: {password}")


if __name__ == '__main__':
    generate_password()
