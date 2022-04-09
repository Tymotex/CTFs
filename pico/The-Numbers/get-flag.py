
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def solve():
    with open('contents.txt', 'r') as f:
        contents = f.read()
        tokens = contents.split(" ")
        for token in tokens:
            try:
                position = int(token)
                print(ALPHABET[position - 1], end="")
            except:
                print(token, end="")
    print()

solve()
