import random
import string

# store alphanumerics + special characters in a list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# function to shuffle the characters, and append to a new list "password"
def get_random_password():
    password_length = int(input("How long would you like the password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(f"Your password is '{password}'")

option = input("Do you want to generate a password? Yes/No ")

if option == "Yes":
    get_random_password()

elif option == "No":
    print("Program ended. Goodbye!")

else:
    print("Invalid input. Please input Yes or No")
    quit()