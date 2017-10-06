# Not solved

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

def solve(n, numbers):
    ret = 0
    dn = n
    w = 1
    print(3 ^ 6)
    print(4 ^ 6)
    print(4 ^ 3)
    for i in range(2*n):
        for j in range(2*n):
            print(bin(i)[2:],bin(j)[2:],bin(i^j)[2:], i^j>2*n)
            print(i^(2*n), j^(2*n))
    # for i in range(n):
    #     if numbers[0]
    # for j in range(n):
    #         if numbers[0][i] ^ numbers[1][j] <= 2*n:
    #             ret += 1
    if ret % 2 == 0:
        return "Karen"
    else:
        return "Koyomi"

def run():
    n = I()
    numbers = [LI() for _ in range(2)]
    print(solve(n, numbers))

run()
