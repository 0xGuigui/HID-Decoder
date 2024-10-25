#!/usr/bin/env python3
"""
Program: HID Decoder
Description: Decodes HID keycodes from a file into readable text.
Usage: python hid_decoder.py <data_file.txt>
Author: 0xGuigui
Date: 2024-10-24
"""

import sys

def splash_screen():
    splash = """
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║             HID Decoder Tool                 ║
    ║           Written by 0xGuigui                ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """
    print(splash)

def main():
    splash_screen()

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <data_file.txt>")
        sys.exit(1)

    data_file = sys.argv[1]

    # HID keycode to character mapping
    keycode_map = {
        0x04: 'a',
        0x05: 'b',
        0x06: 'c',
        0x07: 'd',
        0x08: 'e',
        0x09: 'f',
        0x0A: 'g',
        0x0B: 'h',
        0x0C: 'i',
        0x0D: 'j',
        0x0E: 'k',
        0x0F: 'l',
        0x10: 'm',
        0x11: 'n',
        0x12: 'o',
        0x13: 'p',
        0x14: 'q',
        0x15: 'r',
        0x16: 's',
        0x17: 't',
        0x18: 'u',
        0x19: 'v',
        0x1A: 'w',
        0x1B: 'x',
        0x1C: 'y',
        0x1D: 'z',
        0x1E: '1',
        0x1F: '2',
        0x20: '3',
        0x21: '4',
        0x22: '5',
        0x23: '6',
        0x24: '7',
        0x25: '8',
        0x26: '9',
        0x27: '0',
        0x28: '\n',  # Enter
        0x2C: ' ',    # Space
        0x2D: '-',
        0x2E: '=',
        0x2F: '[',
        0x30: ']',
        0x31: '\\',
        0x33: ';',
        0x34: "'",
        0x36: ',',
        0x37: '.',
        0x38: '/',
        # Add more keycodes if necessary in this list, but in my case, I only need these ones.
    }

    try:
        with open(data_file, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{data_file}' was not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{data_file}': {e}")
        sys.exit(1)

    try:
        # Convert hex codes to a list of integers
        codes = [int(x, 16) for x in data.strip().split()]
    except ValueError:
        print("Error: The data file contains invalid hexadecimal numbers.")
        sys.exit(1)

    # Decode the keycodes into characters
    output = ''
    for code in codes:
        char = keycode_map.get(code, '')
        output += char

    print("\nDecoded Output:\n")
    print(output)

if __name__ == "__main__":
    main()
