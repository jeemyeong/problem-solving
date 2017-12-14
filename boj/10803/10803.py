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

def solve(n, m):
    INF = 987654321
    dp = [[INF]*(n+1) for _ in range(m+1)]
    dp[1][1] = 1
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(m+1):
        dp[i][0] = 0
    for y in range(1, m+1):
        for x in range(1, n+1):
            if (x >= 4 * y):
                dp[y][x] = min(dp[y][x], dp[y][y-x] + 1)
                continue
            if y == x:
                dp[y][x] = 1
                continue
            for dy in range(y+1):
                dp[y][x] = min(dp[y][x], dp[dy][x] + dp[y-dy][x])
            for dx in range(x+1):
                dp[y][x] = min(dp[y][x], dp[y][dx] + dp[y][x-dx])
    return dp[m][n]

# print(solve(6, 5))

def main():
    n, m = LI()
    print(solve(n, m))

main()
