import os
from tkinter import messagebox
from encrypt_decrypt import encrypt_file
from encrypt_decrypt import decrypt_file
from getpass import getpass
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system

app = ctk.CTk()
app.title("Secure File Locker 🔐") 
app.geometry("900x700") 
app.resizable(width=True, height=True)


# while True:
#     print("=======================================")
#     print("           Secure File Locker          ")
#     print("=======================================")
#     print("1. Encrypt File")
#     print("2. Decrypt File")
#     print("3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         filename = input("Enter the path of the file to encrypt (with the file name and extension): ")
#         filename = filename.strip()
#         filename = filename.strip('"')
#         if not os.path.isfile(filename):
#             print("File not found.")
#             continue
#         password = getpass("Enter the password: ")
#         encrypt_file(filename, password)
#     elif choice == "2":
#         filename = input("Enter the path of the file to decrypt (with the file name and extension): ")
#         filename = filename.strip()
#         filename = filename.strip('"')
#         if not os.path.isfile(filename):
#             print("File not found.")
#             continue
#         password = getpass("Enter the password: ")
#         decrypt_file(filename, password)
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please try again.")

def change_theme(): # Function to toggle between light and dark themes
    try:
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    except Exception as e:
        print(f" ❌ Error changing theme: {e}")
        messagebox.showerror("Theme Error", f"Error changing theme: {e}")

def clear_screen(): # Function to clear the current screen by destroying all widgets in the main application window
    try:
        for widget in app.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f" ❌ Error clearing screen: {e}")
        messagebox.showerror("Screen Error", f"Error clearing screen: {e}")

def main_menu(): # Function to display the main menu after successful login or registration
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Welcome to Secure File Locker!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        options = [
            "Encrypt File", "Decrypt File", "Exit"
        ]
        for idx, opt in enumerate(options, 1):
            ctk.CTkButton(app, text=f"{idx}. {opt}", command=lambda i=idx: option_selected(i)).pack(pady=4) # Creates buttons for each option in the main menu
        
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in main menu: {e}")
        messagebox.showerror("Menu Error", f"Error in main menu: {e}")

def encrypt_screen(): # Function to display the encryption screen where user can select a file to encrypt and enter the password
    try:
        clear_screen()
        
        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Encrypt a File", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the path of the file to encrypt (with the file name and extension):").pack(pady=5)
        file_entry = ctk.CTkEntry(app, width=400)
        file_entry.pack(pady=5)

        ctk.CTkLabel(app, text="Enter the password:").pack(pady=5)
        password_entry = ctk.CTkEntry(app, show='*', width=400)
        password_entry.pack(pady=5)

        def encrypt_action():
            filename = file_entry.get().strip().strip('"')
            password = password_entry.get()
            if not os.path.isfile(filename):
                messagebox.showerror("File Error", "File not found.")
                return
            encrypt_file(filename, password)
            messagebox.showinfo("Success", f"File encrypted successfully!\nEncrypted file saved as: {filename}.encrypted")
            main_menu()

        ctk.CTkButton(bottom_frame, text="Back", command=lambda: main_menu()).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in encryption screen: {e}")
        messagebox.showerror("Encryption Screen Error", f"Error in encryption screen: {e}")

def decrypt_screen(): # Function to display the decryption screen where user can select a file to decrypt and enter the password
    try:
        clear_screen()
        
        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)
        
        ctk.CTkLabel(app, text="Decrypt a File", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the path of the file to decrypt (with the file name and extension):").pack(pady=5)
        file_entry = ctk.CTkEntry(app, width=400)
        file_entry.pack(pady=5)

        ctk.CTkLabel(app, text="Enter the password:").pack(pady=5)
        password_entry = ctk.CTkEntry(app, show='*', width=400)
        password_entry.pack(pady=5)

        def decrypt_action():
            filename = file_entry.get().strip().strip('"')
            password = password_entry.get()
            if not os.path.isfile(filename):
                messagebox.showerror("File Error", "File not found.")
                return
            decrypt_file(filename, password)
            messagebox.showinfo("Success", f"File decrypted successfully!\nFile saved as: {filename.replace('.encrypted', '')}")
            main_menu()

        ctk.CTkButton(bottom_frame, text="Back", command=lambda: main_menu()).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in decryption screen: {e}")
        messagebox.showerror("Decryption Screen Error", f"Error in decryption screen: {e}")

def option_selected(option): # Function to handle the option selected by the user in the main menu
    try:
        if option == 1:
            encrypt_screen()
        elif option == 2:
            decrypt_screen()
        elif option == 3:
            app.destroy()
        else:
            messagebox.showerror("Error", "Invalid option selected.")
            main_menu()
    except Exception as e:
        print(f" ❌ Error in option selection: {e}")
        messagebox.showerror("Option Selection Error", f"Error in option selection: {e}")

main_menu() # Start the application by displaying the main menu
app.mainloop()
