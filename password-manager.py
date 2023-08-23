# Import Fernet from cryptography module for encryption and decryption

from cryptography.fernet import Fernet

# Function to load the encryption key from a file
def load_key():
    # Open the key file in binary read mode
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Get the master password from the user
master_pwd = input("What is the master password? ")

# Load the encryption key and combine it with the master password
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# Function to view decrypted passwords
def view():
    # Open the password file in read mode
    with open('password.txt', 'r') as f:
        # Read each line in the file
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")  # Split username and encrypted password
            # Decrypt the password and print
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

# Function to add a new password
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # Open the password file in append mode and write encrypted password
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop to interact with the user
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please choose 'view', 'add', or 'q' to quit.")
        continue
