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

def solve(n, seq):
    hash_table = {}
    for i, e in enumerate(seq):
        if e not in hash_table:
            hash_table[e] = 1
        else:
            hash_table[e] += 1
    ret = []
    for i in hash_table:
        if hash_table[i]%2 == 1:
            ret.append(i)
    return " ".join(map(str, sorted(ret)))

def main():
    t = I()
    for _ in range(t):
        n = I()
        seq = LI()
        print(solve(n, seq))

main()
