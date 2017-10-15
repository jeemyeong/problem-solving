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

def solve(n, s, seq):
    cur = 0
    i = 0
    for j in range(n):
        cur += seq[j]
        while cur > s and i <= j:
            cur -= seq[i]
            i += 1
        if cur == s:
            return str(i+1) + " " + str(j+1)
    return -1

def main():
    t = I()
    for _ in range(t):
        n, s = LI()
        seq = LI()
        print(solve(n, s, seq))

main()
