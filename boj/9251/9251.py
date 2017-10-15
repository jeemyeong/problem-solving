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

def solve(l1, l2):
    dp = [[0]*(len(l2)+1)] + [[0] + [0]*len(l2) for _ in range(len(l1))]
    for i, e1 in enumerate(l1):
        for j, e2 in enumerate(l2):
            if e1 == e2:
                dp[i+1][j+1] = dp[i][j] +1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return dp[len(l1)][len(l2)]

def main():
    l1 = (S())
    l2 = (S())
    print(solve(l1, l2))

main()
