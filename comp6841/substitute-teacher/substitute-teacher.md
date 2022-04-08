# Substitute Teacher

```python
from pwn import *
from math import *

def solve():
    with open("spicy_flag.txt", "r") as f:
        contents = f.read()
        for c in contents:
            print(chr(int(sqrt(ord(c)) - 1)), end="")

solve()
```
