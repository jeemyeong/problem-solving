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

def solve(n, k):
    W = [[0] * (k+1) for _ in range(n+1)]
    W[1] = [i for i in range(k+1)]
    for i in range(2, n+1):
        for j in range(1, k+1):
            W[i][j] = 1 + min(max(W[i-1][x-1], W[i][j-x]) for x in range(1, j+1))
    return W[n][k]

def main():
    T = I()
    for _ in range(T):
        n, k = LI()
        print(solve(n, k))

main()
