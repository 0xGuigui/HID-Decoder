# 🚀 HID Decoder Tool Documentation

## 📝 Overview
The **HID Decoder Tool** is a command-line Python program designed to decode HID (Human Interface Device) keycodes from a text file into readable text. This tool can help interpret HID data from devices like keyboards when presented in raw hexadecimal format.

### 📋 Prerequisites
- Python 3 installed on your system.

## ⚙️ Usage

### Command Structure
To execute the HID Decoder Tool, run the following command in your terminal:
```bash
python HID_Decoder_Tool.py <data_file.txt>
```

#### Arguments
- `<data_file.txt>`: The path to the text file containing HID keycodes.

### Example
```bash
python HID_Decoder_Tool.py keycodes.txt
```

## 🛠️ Program Functions

### `splash_screen()`
Displays a splash screen with the program's name and author. This function serves an introductory purpose when launching the program.

### `main()`
The main entry point of the program, which performs the following tasks:
1. Calls the `splash_screen()` function to display the splash message.
2. Checks for the correct number of command-line arguments.
3. Reads the file specified by the user and processes each HID keycode line-by-line.

## 🔑 Keycode Mapping
The tool uses a pre-defined dictionary mapping HID keycodes to their corresponding characters. This dictionary currently supports lowercase alphabet characters, and can be extended to include additional keycodes as needed.

Example of HID keycode mappings:
```python
keycode_map = {
    0x04: 'a',
    0x05: 'b',
    0x06: 'c',
    ...
}
```

## 🐛 Error Handling
The program checks for:
- Incorrect number of arguments.
- Missing or inaccessible input files.
When these errors occur, a usage message is displayed to guide the user.

---

*Authored by 0xGuigui*