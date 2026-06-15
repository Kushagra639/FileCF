import os
from encrypt_decrypt import encrypt_file
from encrypt_decrypt import decrypt_file
from getpass import getpass

while True:
    print("="*40)
    print("     File CF - Secure File Locker 🔐")
    print("="*40)
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the path of the file to encrypt (with the file name and extension): ")
        filename = filename.strip()
        filename = filename.strip('"')
        if not os.path.isfile(filename):
            print("File not found.")
            continue
        password = getpass("Enter the password: ")
        encrypt_file(filename, password)
    elif choice == "2":
        filename = input("Enter the path of the file to decrypt (with the file name and extension): ")
        filename = filename.strip()
        filename = filename.strip('"')
        if not os.path.isfile(filename):
            print("File not found.")
            continue
        password = getpass("Enter the password: ")
        decrypt_file(filename, password)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
