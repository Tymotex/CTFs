import re

def get_num(line):
    pattern = re.compile('(\d+)')
    result = pattern.search(line)
    return int(result.group(1))

def solve():
    with open("shuffle.txt", "r") as f:
        lines = f.readlines()
        lines.sort(key=get_num)
        for line in lines:
            print(re.sub(r"::\d+::", "", line))

solve()