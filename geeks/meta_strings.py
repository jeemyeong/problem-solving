# http://practice.geeksforgeeks.org/problems/meta-strings/0
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

def solve(a, b):
    ret = 0
    conflict = []
    for i, e in enumerate(a):
        if a[i] == b[i]:
            continue
        else:
            conflict.append((a[i], b[i]))
    if len(conflict) == 2 and conflict[0][1] == conflict[1][0] and conflict[0][0] == conflict[1][1]:
        return 1
    return 0

def main():
    t = I()
    for _ in range(t):
        a = S()
        b = S()
        print(solve(a, b))

main()
