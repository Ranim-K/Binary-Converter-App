import pyfiglet
from colorama import Fore
import inquirer
import os

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Binary Converter")
    print(Fore.BLUE + ascii_art)

def text_to_binary():
    while True:
        questions = [
            inquirer.List('choice',
                          message="Welcome to Binary Converter",
                          choices=[
                              ("1. Convert A String", "1"),
                              ("2. Convert A file", "2"),
                              ("Exit", "3")
                          ],
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']
        if choice == "1":
            text = input("Text: ")
            res = ''.join(format(ord(i), '08b') for i in text)
            print("The Text after binary Conversion: " + str(res))
        elif choice == "2":
            try:
                input_file = input(r"Input File Path: ")
                if not os.path.isfile(input_file):
                    raise FileNotFoundError(f"File '{input_file}' not found.")
                
                output_file = os.path.splitext(input_file)[0] + "_binary.txt"
                
                with open(input_file, 'r', encoding="utf-8") as files:
                    text = files.read()
                    res = ''.join(format(ord(i), '08b') for i in text)
                    
                with open(output_file, 'wb') as file:
                    file.write(res.encode('utf-8'))
                
                print(f"Successfully converted '{input_file}' to binary and saved as '{output_file}'")
            except FileNotFoundError as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        elif choice == "3":
            print("Exiting...")
            break

def binary_to_text():
    while True:
        questions = [
            inquirer.List('choice',
                          message="Welcome to Binary Converter",
                          choices=[
                              ("1. Convert Binary String", "1"),
                              ("2. Convert Binary File", "2"),
                              ("Exit", "3")
                          ],
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']
        if choice == "1":
            binary = input("Binary: ")
            text = ""
            for i in range(0, len(binary), 8):
                byte = binary[i:i+8]
                text += chr(int(byte, 2))
            print("The Binary after text Conversion: " + text)
        elif choice == "2":
            try:
                input_file = input(r"Input Binary File Path: ")
                if not os.path.isfile(input_file):
                    raise FileNotFoundError(f"File '{input_file}' not found.")
                
                output_file = os.path.splitext(input_file)[0] + "_text.txt"
                
                with open(input_file, 'rb') as files:
                    binary = files.read().decode('utf-8')
                    text = ""
                    for i in range(0, len(binary), 8):
                        byte = binary[i:i+8]
                        text += chr(int(byte, 2))
                        
                with open(output_file, 'w', encoding="utf-8") as file:
                    file.write(text)
                
                print(f"Successfully converted '{input_file}' from binary to text and saved as '{output_file}'")
            except FileNotFoundError as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        elif choice == "3":
            print("Exiting...")
            break

def main():
    while True:
        display_ascii_art()
        questions = [
            inquirer.List('choice',
                          message="Welcome to Binary Converter",
                          choices=[
                              ("1. Text to Binary", "1"),
                              ("2. Binary to Text", "2"),
                              ("Exit", "3")
                          ],
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']
        if choice == "1":
            text_to_binary()
        elif choice == "2":
            binary_to_text()
        elif choice == "3":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
