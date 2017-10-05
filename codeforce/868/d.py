# Not solved

import sys
read = sys.stdin.readline

def solve(n, numbers, m, concatenation):
    for a, b in concatenation:
        numbers.append(numbers[a-1] + numbers[b-1])
    print(numbers)
    for i in range(n, n+m):
        cur = numbers[i]
        print(cur)
        str_zero = "0"
        str_one = "1"
        find = cur.find(str_zero)
        while find != -1:
            str_zero += "0"
            find = cur.find(str_zero)
        find = cur.find(str_one)
        while find != -1:
            str_one += "1"
            find = cur.find(str_one)
        print(str_one, str_zero)
        print(str(min(len(str_zero)-1, len(str_one)-1)))

def run():
    n = int(read().replace("\n", "").replace("\r\n", ""))
    numbers = []
    for _ in range(n):
        numbers.append(read().replace("\n", "").replace("\r\n", ""))
    m = int(read().replace("\n", "").replace("\r\n", ""))
    concatenation = []
    for _ in range(m):
        concatenation.append(list(map(int, read().replace("\n", "").replace("\r\n", "").split())))
    solve(n, numbers, m, concatenation)

run()
