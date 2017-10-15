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

def find_lower(sequence, e):
    for i, item in enumerate(sequence):
        if item >= e:
            return i
    return len(sequence)

def solve(n, sequence):
    LSI = []
    P = []
    for i, item in enumerate(sequence):
        lower_bound = find_lower(LSI, item)
        if len(LSI) == lower_bound:
            LSI.append(item)
        else:
            LSI[lower_bound] = item
        P.append(lower_bound)
    size = len(LSI)
    ans = []
    for i in range(n-1, -1, -1):
        if size < 0:
            break
        if P[i] == size-1:
            ans.insert(0, sequence[i])
            size -= 1
    return len(ans)

def main():
    n = I()
    sequence = LI()
    print(solve(n, sequence))

main()