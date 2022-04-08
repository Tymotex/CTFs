import binascii



if __name__ == "__main__":
    with open("codepoints", "r") as codepoints_file:
        codepoints = codepoints_file.read()
        hex_codes = [i for i in codepoints.split("%u")] 
        print(hex_codes)
        for each_code in hex_codes:
            binary_str = binascii.unhexlify(each_code)
            print(binary_str.decode(), end="")
