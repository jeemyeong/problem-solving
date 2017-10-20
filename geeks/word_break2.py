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

def solve(N, words, s):
    words = set(words)
    dp = [[] for _ in range((len(s)+1))] 
    dp[0] = [[]]
    for i in range(len(s)+1):
        for j in range(1, 15):
            if i-j >= 0 and len(dp[i-j]) > 0 and s[i-j:i] in words:
                for e_in_dp in dp[i-j]:
                    dp[i].append(e_in_dp + [s[i-j:i]])
    return ("(" + ")(".join(sorted([" ".join(dp[-1][i]) for i, e in enumerate(dp[-1])])) + ")")

def main():
    T = I()
    for _ in range(T):
        N = I()
        words = LS()
        s = S()
        print(solve(N, words, s))

main()
