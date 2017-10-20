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

def solve(N, s, words):
    words = set(words)
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(len(s)+1):
        for j in range(1, 15):
            if i-j >= 0 and dp[i-j] is True and s[i-j:i] in words:
                dp[i] = True
    return 1 if dp[len(s)] else 0

def main():
    T = I()
    for _ in range(T):
        N = I()
        words = LS()
        s = S()
        print(solve(N, s, words))

main()
