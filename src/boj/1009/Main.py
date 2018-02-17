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

def solve(a, b):
    if a % 10 in (1, 5, 6):
        return a % 10
    if a % 10 == 0:
        return 10
    if b % 2 == 0:
        return solve(a**2, b//2)
    else:
        return (solve(a**2, b//2) * a) % 10

def main():
    n = I()
    for _ in range(n):
        a, b = LI()
        print(solve(a, b))

main()
