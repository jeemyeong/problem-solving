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

def get_item_without_null_exception(i, k, p, dp):
    if i < 0 or k < 0 or p < 0:
        return 0
    else:
        return dp[i][k][p]

def solve(T, W, order):
    dp = [[[0]*2 for _ in range(W+1)] for _ in range(T)]

    for i in range(0, T):
        for k in range(W+1):
            if order[i] == 1:
                dp[i][k][0] = max(get_item_without_null_exception(i-1, k, 0, dp), get_item_without_null_exception(i-1, k-1, 1, dp)) + 1
                dp[i][k][1] = max(get_item_without_null_exception(i-1, k, 1, dp), get_item_without_null_exception(i-1, k-1, 0, dp))
            else:
                dp[i][k][0] = max(get_item_without_null_exception(i-1, k, 0, dp), get_item_without_null_exception(i-1, k-1, 1, dp))
                dp[i][k][1] = max(get_item_without_null_exception(i-1, k, 1, dp), get_item_without_null_exception(i-1, k-1, 0, dp)) + 1
    return max(max(dp[T-1], key=lambda x: max(x)))

def run():
    T, W = LI()
    order = [I() for _ in range(T)]
    print(solve(T, W, order))

run()
