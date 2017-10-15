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

def merge(n1, n2):
    return int(str(n1)+str(n2))

def solve(n, m, a, b):
    ret = []
    for i in range(1, 10):
        if i in a and i in b:
            ret.append(i)
    ret.append(merge(min(a), min(b)))
    ret.append(merge(min(b), min(a)))
    
    return min(ret)

def main():
    n, m = LI()
    a = LI()
    b = LI()
    print(solve(n, m, a, b))

main()
