import os
from encrypt_decrypt import encrypt_file
from encrypt_decrypt import decrypt_file

while True:
    print("=======================================")
    print("           Secure File Locker          ")
    print("=======================================")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        file = input("Enter the path of the file to encrypt (with the file name and extension): ")
        file = file.strip()
        file = file.strip('"')
        password = input("Enter the password: ")
        encrypt_file(file, password)
    elif choice == "2":
        file = input("Enter the path of the file to decrypt (with the file name and extension): ")
        file = file.strip()
        file = file.strip('"')
        password = input("Enter the password: ")
        decrypt_file(file, password)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")