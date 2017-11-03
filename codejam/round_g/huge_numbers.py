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

def solve(A, N, P):
    C = A%P
    ans = 1
    for i in range(N, 0, -1):
        for j in range(i):
            ans = ans * C % P
    return ans

def main():
    T = I()
    for _ in range(T):
        A, N, P = LI()
        print(solve(A, N, P))

main()
