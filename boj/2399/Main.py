import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(n, x):
    x.sort()
    accumulate = x[0]
    ret = 0
    for i in range(1, n):
        cur = x[i]
        ret += cur * i - accumulate
        accumulate += cur
    return ret * 2

def main():
    n = I()
    x = LI()
    print(solve(n, x))

main()
