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

def solve(n, m, dp):
    if dp[(n, m)] != inf:
        return dp[(n, m)]
    if n < 1 or m < 1:
        return inf
    if n < m:
        return solve(m, n, dp)
    if n == m:
        dp[(n, m)] = 1
        return dp[(n, m)]
    if n % m == 0:
        dp[(n, m)] = n // m
        return dp[(n, m)]
    if (n >= 3 * m):
        dp[(n, m)] = min(dp[(n, m)], solve(n-m, m, dp) + 1)
    else:
        for dm in range(1, (m+1)//2+1):
            dp[(n, m)] = min(dp[(n, m)], solve(n, dm, dp) + solve(n, m-dm, dp))
        for dn in range(1, (n+1)//2+1):
            dp[(n, m)] = min(dp[(n, m)], solve(dn, m, dp) + solve(n-dn, m, dp))
    return dp[(n, m)]

# print(solve(6, 5))

def main():
    n, m = LI()
    dp = {}
    for i in range(10001):
        for j in range(101):
            dp[(i, j)] = inf
    print(solve(n, m, dp))

main()
