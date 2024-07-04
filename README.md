# Binary Converter App

A user-friendly application for converting text to binary and vice versa. This repository includes two versions of the app: one with a graphical user interface (GUI) built with Tkinter and one without a GUI, which runs in the command line.

## Features

- **Text to Binary Conversion**
- **Binary to Text Conversion**
- **File Conversion**:
  - Convert text files to binary files
  - Convert binary files to text files
- **Clipboard Copying** (GUI version)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ranim-K/Binary-Converter-App.git
    cd binary-converter-app
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` should contain:

    ```
    pyfiglet
    pyperclip
    colorama
    inquirer
    ```

## Usage

### GUI Version

1. **Run the GUI application:**

    ```bash
    python binary_converter_gui.py
    ```

2. **Using the GUI:**

    - **Text to Binary Conversion:**
        - Enter the text in the "Text to Binary" section.
        - Click "Convert" to see the binary output.
        - Click "Copy" to copy the binary output to the clipboard.

    - **Binary to Text Conversion:**
        - Enter the binary string in the "Binary to Text" section.
        - Click "Convert" to see the text output.
        - Click "Copy" to copy the text output to the clipboard.

    - **File Conversion:**
        - Click "Text to Binary File" to convert a text file to a binary file.
        - Click "Binary to Text File" to convert a binary file to a text file.

### Non-GUI Version

1. **Run the command line application:**

    ```bash
    python binary_converter_cli.py
    ```

2. **Using the Command Line Interface:**

    - **Text to Binary Conversion:**
        - Select "Text to Binary" from the menu.
        - Choose to convert a string or a file.
        - Follow the prompts to enter the text or file path.

    - **Binary to Text Conversion:**
        - Select "Binary to Text" from the menu.
        - Choose to convert a binary string or a file.
        - Follow the prompts to enter the binary string or file path.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Your Name]

## Acknowledgments

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI package.
- [pyfiglet](https://github.com/pwaller/pyfiglet) - A full port of FIGlet (a program for making large letters out of ordinary text).
- [pyperclip](https://github.com/asweigart/pyperclip) - A cross-platform clipboard module for Python.
- [colorama](https://github.com/tartley/colorama) - A package to produce colored terminal text.
- [inquirer](https://github.com/magmax/python-inquirer) - A collection of common interactive command line user interfaces.

