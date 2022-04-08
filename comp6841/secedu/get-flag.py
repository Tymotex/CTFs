from pwn import *
import re

def solve():
    with open("secedu.txt", "r") as f:
        contents = f.read()
        tokens = contents.split(" ")
        for token in tokens:
            token = re.sub(r"sec", "0", token)
            token = re.sub(r"edu", "1", token)
            print(unhex(hex(int(token, 2))[2:]).decode(), end="")
        print()
solve()
