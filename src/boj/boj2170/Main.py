import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(lst):
    lst = sorted(lst)
    _to = -1000000000
    length = 0
    for a, b in lst:
        if b > _to:
           length += (b - max(a, _to))
           _to = b
    return length

def main():
    n = I()
    lst = []
    for _ in range(n):
        a, b = LI()
        lst.append((a, b))
    print(solve(lst))

main()
