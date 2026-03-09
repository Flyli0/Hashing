import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from tkinter import ttk

from SHA256.SecureHashingAlgorithm import sha_256
from SHA512.SecureHashingAlgorithm import sha_512
from PBKDF2.PBKDF2 import pbkdf2
from Passwords.Storage_service import password_storage
from Passwords.generator import generate


class CryptoGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hashing Toolkit")
        self.root.geometry("400x300")

        tk.Label(self.root,
                 text="Hashing Toolkit",
                 font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root,
                  text="Hash Text / File",
                  bg="#42FF1C",
                  font=("Arial", 12, "bold"),
                  width=25,
                  command=self.encrypt_text_file).pack(pady=10)

        tk.Button(self.root,
                  text="Hash Password",
                  bg="#FAF25F",
                  font=("Arial", 12, "bold"),
                  width=25,
                  command=self.encrypt_password).pack(pady=10)

        tk.Button(self.root,
                  text="Save Password",
                  bg="#FFB700",
                  font=("Arial", 12, "bold"),
                  width=25,
                  command=self.save_password).pack(pady=10)

        self.root.mainloop()

    # TEXT / FILE HASHING

    def encrypt_text_file(self):
        window = tk.Toplevel(self.root)
        window.title("Hash Text or File")
        window.geometry("400x300")

        tk.Label(window, text="Enter Text").pack()

        text_entry = tk.Text(window, height=5)
        text_entry.pack()

        sha_var = tk.StringVar(value="sha256")

        tk.Radiobutton(window, text="SHA-256", variable=sha_var, value="sha256").pack()
        tk.Radiobutton(window, text="SHA-512", variable=sha_var, value="sha512").pack()

        def encrypt_action():
            message = text_entry.get("1.0", tk.END).encode()
            selected_sha = sha_var.get()
            if selected_sha == "sha256":
                result = sha_256(message)
            else:
                result = sha_512(message)

            messagebox.showinfo("Result", f"Hashed ({selected_sha}): {result.hex()}")

        tk.Button(window,
                  text="Hash",
                  command=encrypt_action).pack(pady=10)

        def open_file():
            filename = filedialog.askopenfilename()

            if filename:
                with open(filename, "rb") as f:
                    data = f.read()

                selected_sha = sha_var.get()
                if selected_sha == "sha256":
                    result = sha_256(data)
                else:
                    result = sha_512(data)

                save_path = filedialog.asksaveasfilename()

                if save_path:
                    with open(save_path, "w") as f:
                        f.write(result.hex())
                messagebox.showinfo("Result", f"File Hashed ({selected_sha}): {result.hex()}")

        tk.Button(window,
                  text="Choose File",
                  command=open_file).pack(pady=10)

    # PASSWORD ENCRYPTION

    def encrypt_password(self):
        window = tk.Toplevel(self.root)
        window.title("Password Hashing")
        window.geometry("400x250")

        tk.Label(window, text="Password").pack()
        password_entry = tk.Entry(window, show="*")
        password_entry.pack()

        tk.Label(window, text="Iterations").pack()
        iter_entry = tk.Entry(window)
        iter_entry.insert(0, "100000")
        iter_entry.pack()

        def encrypt_action():
            password = password_entry.get().encode()
            iterations = int(iter_entry.get())

            salt = generate(128)
            hash_value = pbkdf2(password, salt, iterations, len(password))

            window = tk.Toplevel(self.root)
            window.title = "Result"
            text = tk.Text(window, height=10, width=40)
            text.pack()

            text.insert("1.0", f"RESULT:  {hash_value.hex()}")
            text.config(state="disabled")


        tk.Button(window,
                  text="Hash Password",
                  command=encrypt_action).pack(pady=10)

    # ============================
    # PASSWORD STORAGE
    # ============================

    def save_password(self):
        window = tk.Toplevel(self.root)
        window.title("Save Password")

        tk.Label(window, text="Username").pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="Key").pack()
        key_entry = tk.Entry(window)
        key_entry.pack()

        progress = ttk.Progressbar(window, orient="horizontal",
                                   length=200, mode="determinate")
        progress.pack(pady=10)

        def save_action():
            name = name_entry.get()
            key = key_entry.get()

            password_storage(name, key)

            messagebox.showinfo("Success", "Password saved!")
            window.destroy()

        tk.Button(window,
                  text="Save",
                  command=save_action).pack(pady=10)


if __name__ == "__main__":
    CryptoGUI()
