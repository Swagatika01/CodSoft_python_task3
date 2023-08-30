import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()

    def generate_password(self):
        length = self.length_var.get()
        include_digits = self.include_digits_var.get()
        include_special_chars = self.include_special_chars_var.get()

        characters = string.ascii_letters
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Password Generator", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        title_label.pack(pady=(20, 10))

        self.length_label = tk.Label(self.root, text="Password Length:", font=("Helvetica", 14), bg="#f0f0f0")
        self.length_label.pack()

        self.length_var = tk.IntVar()
        self.length_entry = tk.Entry(self.root, textvariable=self.length_var, font=("Helvetica", 14))
        self.length_entry.pack()

        self.include_digits_var = tk.BooleanVar()
        self.include_digits_checkbutton = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits_var, font=("Helvetica", 14), bg="#f0f0f0")
        self.include_digits_checkbutton.pack()

        self.include_special_chars_var = tk.BooleanVar()
        self.include_special_chars_checkbutton = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.include_special_chars_var, font=("Helvetica", 14), bg="#f0f0f0")
        self.include_special_chars_checkbutton.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password, font=("Helvetica", 16), bg="#007bff", fg="white")
        self.generate_button.pack(pady=20)

        result_frame = tk.Frame(self.root, bg="#dcdcdc")
        result_frame.pack(padx=20, pady=20, fill="both")

        self.password_var = tk.StringVar()
        self.password_label = tk.Label(result_frame, textvariable=self.password_var, font=("Courier", 16), bg="#dcdcdc", relief="solid", bd=3, padx=20, pady=20, borderwidth=2, highlightcolor="beige")
        self.password_label.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
