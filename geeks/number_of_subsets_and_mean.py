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

def solve(N, A):
    max_of_A = max(A)
    min_of_A = min(A)
    # A.count(max_of_A), A.count(min_of_A)
    return str((2**A.count(max_of_A)-1)%mod) + " " + str((2**A.count(min_of_A)-1)%mod)

def main():
    T = I()
    for _ in range(T):
        N = I()
        A = LI()
        print(solve(N, A))

main()
