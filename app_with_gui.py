import tkinter as tk
from tkinter import filedialog, messagebox
import pyfiglet
import os
import pyperclip

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Converter")
        self.create_widgets()

    def create_widgets(self):
        ascii_art = pyfiglet.figlet_format("Binary Converter")
        ascii_label = tk.Label(self.root, text=ascii_art, font=("Courier", 12), fg="blue")
        ascii_label.grid(row=0, column=0, columnspan=4)

        self.text_var = tk.StringVar()
        self.binary_var = tk.StringVar()

        # Text to Binary Section
        tk.Label(self.root, text="Text to Binary").grid(row=1, column=0, columnspan=4)
        tk.Entry(self.root, textvariable=self.text_var, width=50).grid(row=2, column=0, columnspan=3)
        tk.Button(self.root, text="Convert", command=self.text_to_binary).grid(row=2, column=3)
        self.binary_label = tk.Label(self.root, textvariable=self.binary_var, width=50, wraplength=400)
        self.binary_label.grid(row=3, column=0, columnspan=3)
        tk.Button(self.root, text="Copy", command=self.copy_binary).grid(row=3, column=3)

        # Binary to Text Section
        tk.Label(self.root, text="Binary to Text").grid(row=4, column=0, columnspan=4)
        self.binary_input = tk.Entry(self.root, width=50)
        self.binary_input.grid(row=5, column=0, columnspan=3)
        tk.Button(self.root, text="Convert", command=self.binary_to_text).grid(row=5, column=3)
        self.text_output = tk.Label(self.root, width=50, wraplength=400)
        self.text_output.grid(row=6, column=0, columnspan=3)
        tk.Button(self.root, text="Copy", command=self.copy_text).grid(row=6, column=3)

        # File Conversion Section
        tk.Label(self.root, text="File Conversion").grid(row=7, column=0, columnspan=4)
        tk.Button(self.root, text="Text to Binary File", command=self.text_file_to_binary).grid(row=8, column=0, columnspan=4)
        tk.Button(self.root, text="Binary to Text File", command=self.binary_file_to_text).grid(row=9, column=0, columnspan=4)

    def text_to_binary(self):
        text = self.text_var.get()
        if text:
            binary = ''.join(format(ord(i), '08b') for i in text)
            self.binary_var.set(binary)
        else:
            messagebox.showwarning("Input Error", "Please enter some text to convert.")

    def binary_to_text(self):
        binary = self.binary_input.get()
        if binary:
            try:
                text = "".join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])
                self.text_output.config(text=text)
            except ValueError:
                messagebox.showwarning("Input Error", "Invalid binary input. Ensure it's a valid binary string.")
        else:
            messagebox.showwarning("Input Error", "Please enter a binary string to convert.")

    def text_file_to_binary(self):
        input_file = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])
        if input_file:
            try:
                with open(input_file, 'r', encoding="utf-8") as file:
                    text = file.read()
                    binary = ''.join(format(ord(i), '08b') for i in text)
                    output_file = os.path.splitext(input_file)[0] + "_binary.txt"
                    with open(output_file, 'wb') as file:
                        file.write(binary.encode('utf-8'))
                    messagebox.showinfo("Success", f"Converted '{input_file}' to binary and saved as '{output_file}'")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def binary_file_to_text(self):
        input_file = filedialog.askopenfilename(title="Select Binary File", filetypes=[("Text Files", "*.txt")])
        if input_file:
            try:
                with open(input_file, 'rb') as file:
                    binary = file.read().decode('utf-8')
                    text = "".join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])
                    output_file = os.path.splitext(input_file)[0] + "_text.txt"
                    with open(output_file, 'w', encoding="utf-8") as file:
                        file.write(text)
                    messagebox.showinfo("Success", f"Converted '{input_file}' from binary to text and saved as '{output_file}'")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def copy_binary(self):
        binary_text = self.binary_var.get()
        if binary_text:
            pyperclip.copy(binary_text)
            messagebox.showinfo("Copied", "Binary text copied to clipboard")
        else:
            messagebox.showwarning("Copy Error", "No binary text to copy")

    def copy_text(self):
        text = self.text_output.cget("text")
        if text:
            pyperclip.copy(text)
            messagebox.showinfo("Copied", "Text copied to clipboard")
        else:
            messagebox.showwarning("Copy Error", "No text to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()
