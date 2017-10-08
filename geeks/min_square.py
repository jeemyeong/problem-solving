# http://practice.geeksforgeeks.org/problems/min-cut-square/0
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

def solve(a, b, dp):
    if (a, b) in dp:
        return dp[(a, b)]
    if a == b:
        dp[(a, b)] = 1
        return 1
    ret = inf
    for i in range(1, a//2+1):
        ret = min(solve(i, b, dp) + solve(a-i, b, dp), ret)
    for i in range(1, b//2+1):
        ret = min(solve(a, i, dp) + solve(a, b-i, dp), ret)
    dp[(a, b)] = ret
    return ret

def main():
    t = I()
    dp = dict()
    for _ in range(t):
        a, b = LI()
        print(solve(a, b, dp))
main()
