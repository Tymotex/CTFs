#!/usr/bin/python3

def map(hex_str):
    if len(hex_str) % 2 == 1:
        hex_str = hex_str + " "
    i = 0
    while i < len(hex_str):
        left_hex_dig = hex_str[i]
        right_hex_dig = hex_str[i + 1]
        ascii_code = int(left_hex_dig + right_hex_dig, 16)
        print(chr(ascii_code), end="")
        i += 2

if __name__ == "__main__":
    map("434f4d507b495f684f70455f7930755f4152335f7761726d65645f325f66696e645f6d3072455f4631616773217d")
