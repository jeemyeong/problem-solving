import sys
# import heapq, collections

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def solve(n):
    if n < 4 or n == 5 or n == 7:
        return -1
    if n == 4 or n == 6:
        return 1
    ret = n // 4
    mod = n % 4
    if mod == 2 or mod == 0:
        return ret
    if mod == 3 or mod == 1:
        return ret-1

def main():
    q = I()
    for _ in range(q):
        print(solve(I()))

main()

