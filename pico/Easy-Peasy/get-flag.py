from pwn import *
import re

context.log_level = "critical"

# def solve():
#     # 
#     flag = "picoCTF{XXXXXXXXXXXXXXXXXXXXXXX}"
#     proc = remote('mercury.picoctf.net', 64260)
#     output = proc.recvrepeat(1)

#     for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
#         flag = c + flag[1:]
#         print("===== Testing: {} =====".format(flag))
#         proc.sendline(flag.encode())
#         output = proc.recvrepeat(1)

#         pattern = re.compile("([0-9a-f]{64})")
#         search_result = pattern.search(output.decode())
#         cipher = search_result.group(1)
#         print(cipher)

#         if cipher[0] == "5" and cipher[1] == "1":
#             print("FOUND ANSWER TO FIRST CHAR: {}".format(flag))

#     proc.close()

def solve():
    proc = remote('mercury.picoctf.net', 64260)
    output = proc.recvrepeat(1)

    for i in range(0, 49):
        proc.sendline(("a" * 1000).encode())

    proc.sendline(("a" * 968).encode())
    
    proc.interactive()

    proc.close()

if __name__ == "__main__":
    solve()
