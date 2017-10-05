import sys
read = sys.stdin.readline

def solve(string, n, lst):
    if string in lst:
        return "YES"
    find_first = False
    find_second = False
    for each in lst:
        if string[0] == each[1]:
            find_first = True
        if string[1] == each[0]:
            find_second = True
    if find_first and find_second:
        return "YES"
    return "NO"

def run():
    string = read().replace("\n", "")
    n = int(read().replace("\n", ""))
    lst = []
    for _ in range(n):
        lst.append(read().replace("\n", ""))
    print(solve(string, n, lst))

run()